#!/usr/bin/env python
# coding:utf-8
import json
import sys
import urllib
from time import sleep
 
import requests as req

 
reload(sys)
sys.setdefaultencoding('utf-8')
 
 
class ZoomEye(object):
    """ uses ZoomEye's API for bulk search and saves the results locally
    """
 
    def __init__(self, host="api.zoomeye.org"):
        self._base_uri = "http://%s" % host
        self._headers = {"Authorization" : "JWT %s" % self.get_token(),
                        "Content-Type": "application/json"}
 
    def get_token(self):
        """
                 Get the authorized token of ZoomEye
        """
                 # payload = {"username": "Your ZoomEye account", "password": "Your ZoomEye password"}
        try:
            res = req.post('https://api.zoomeye.org/user/login',
                           data=json.dumps(payload))
        except Exception as e:
            print e
            sys.exit()
        return json.loads(res.text)['access_token']
 
    def resource_info(self):
        """
                 See how many remaining query results are available in the current month
        """
        return req.get("https://api.zoomeye.org/resources-info", headers=self._headers).content
 
    def get_content(self, searchtype, keyword, startpage, endpage):
        '''
                 Get the query content
        '''
        for i in xrange(startpage, endpage + 1):
            print "Get page " + str(i) + " info ..."
            uri = 'https://api.zoomeye.org/%s/search?query=%s&page=%s&fact=app,os' % (
                searchtype, urllib.quote(keyword), i)
            try:
                result_page = req.get(uri, headers=self._headers)
                page_content = json.loads(result_page.content)
            except Exception as e:
                print e
            print type(page_content)
            if result_page.status_code == 200:
                                 # Search has two types, one is host and the other is web service.
                if searchtype == 'host':
                    for match in page_content['matches']:
                        # print match
                                                 #  host search results, here you can see the return package customization
                        res_line = match['ip'] + ':' + str(match['portinfo']['port']) + '\t' + match[
                            'portinfo']['banner'].strip() + '\t' + match['geoinfo']['isp']
                        print res_line
                        self.save_result(res_line)
                elif searchtype == 'web':
                    for match in page_content['matches']:
                                                 #   web search results, here you can see the return package customization
                        res_line = match['ip'][
                            0] + '\t' + match['title'] + '\t' + 'http://' + match['site']
                        print match['ip'][0] + '\t' + 'http://' + match['site']
                        self.save_result(str(res_line).encode('utf-8'))
            else:
                print "Error Code: %s" % result_page.status_code, result_page.content
            sleep(0.2)
 
    def search(self, keyword, page=1, searchtype="web"):
                 '''Execute query operation'''
        uri = 'https://api.zoomeye.org/%s/search?query=%s&page=%s&fact=app,os' % (
            searchtype, urllib.quote(keyword), page)
        pages = self.get_pages(uri)
                 # Execute query operation
        self.get_content(searchtype=searchtype, keyword=keyword,
                         startpage=page, endpage=pages)
 
    def save_result(self, res):
                 '''Write the result to the file '''
        with open('result.txt', 'a') as f:
            f.writelines(res + '\n')
 
    def get_pages(self, uri):
                 '''Paging the search results'''
        try:
            response = req.get(uri, headers=self._headers)
            search_res = json.loads(response.content)
            print response.url
        except Exception as e:
            print e
                 # here to determine whether there is a search result, if the response code is 200 to indicate the request to the result and return the number of pages, otherwise print error message
        if response.status_code == 200:
            total = int(search_res['total'])
            page = total / 10
            if total % 10 == 0:
                return page
            print page
            return page + 1
        else:
            print "Error Code: ", response.status_code, "Tips: ", search_res
            sys.exit()
 
if __name__ == "__main__":
    zoomeye = ZoomEye()
         # See how many remaining query results are available in the current month
    print zoomeye.resource_info()
         # Inquire
    print zoomeye.search("city:jinan struts2", searchtype="web", page=1)