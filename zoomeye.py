#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014-2016 ZoomEye Developers (https://www.zoomeye.org)
"""

__author__ = "nixawk"
__version__ = "1.0.0"
__license__ = "GPL-2.0"
__description__ = ("ZoomEye is a search engine for cyberspace "
                   "that lets the user find specific network components"
                   "(ip, services, etc.).")
__classes__ = ["ZoomEye"]
__funcs__ = [
    "login",
    "dork_search",
    "resources_info",
    "show_site_ip",
    "show_ip_port",
    "zoomeye_api_test"
]


import requests
import getpass
import sys
import time

pagenum = 3

#IP + Site array
iparr = []
geoarr = []

raw_input = raw_input if sys.version_info.major <= 2 else input


class ZoomEye(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

        self.token = ''
        self.zoomeye_login_api = "https://api.zoomeye.org/user/login"
        self.zoomeye_dork_api = "https://api.zoomeye.org/{}/search"
        self.zoomeye_history_api = "https://api.zoomeye.org/both/search?history=true&ip={}"

    def login(self):
        """Please access https://www.zoomeye.org/api/doc#login
        """
        data = '{{"username": "{}", "password": "{}"}}'.format(self.username,
                                                               self.password)
        resp = requests.post(self.zoomeye_login_api, data=data)
        if resp and resp.status_code == 200 and 'access_token' in resp.json():
            self.token = resp.json().get('access_token')
        return self.token

    def dork_search(self, dork, page=1, resource='web', facet=['ip']):
        """Search records with ZoomEye dorks.

        param: dork
               ex: country:cn
               access https://www.zoomeye.org/search/dorks for more details.
        param: page
               total page(s) number
        param: resource
               set a search resource type, ex: [web, host]
        param: facet
               ex: [app, device]
               A comma-separated list of properties to get summary information
        """
        result = []
        if isinstance(facet, (tuple, list)):
            facet = ','.join(facet)

        zoomeye_api = self.zoomeye_dork_api.format(resource)
        headers = {'Authorization': 'JWT %s' % self.token}
        params = {'query': dork, 'page': page + 1, 'facet': facet}
        resp = requests.get(zoomeye_api, params=params, headers=headers)
        if resp and resp.status_code == 200 and 'matches' in resp.json():
            matches = resp.json().get('matches')
            # total = resp.json().get('total')  # all matches items num
            result = matches

            # Every match item incudes the following information:
            # geoinfo
            # description
            # check_time
            # title
            # ip
            # site
            # system
            # headers
            # keywords
            # server
            # domains

        return result
        
        
    def history_ip(self, ip):
        """Query IP History Information .

        param: ip
        """
        result = []

        zoomeye_api = self.zoomeye_history_api.format(ip)
        headers = {'Authorization': 'JWT %s' % self.token}
        resp = requests.get(zoomeye_api, headers=headers)
        if resp and resp.status_code == 200 and 'data' in resp.json():
            matches = resp.json()
            print(matches.get('count'))
            result = matches
        return result

    def resources_info(self):
        """Resource info shows us available search times.

        host-search: total number of available host records to search
        web-search: total number of available web records to search
        """
        data = None
        zoomeye_api = "https://api.zoomeye.org/resources-info"
        headers = {'Authorization': 'JWT %s' % self.token}
        resp = requests.get(zoomeye_api, headers=headers)
        if resp and resp.status_code == 200 and 'plan' in resp.json():
            data = resp.json()

        return data


def show_site_ip(data):
    if data:
        for i in data:
            ips = (i.get('site'), i.get('ip'))
            iparr.append(ips)
            #geo = (i.get('geoinfo'))

            #return ips
            #print(i.get('site'), i.get('ip'))
            #print(i.get('geoinfo'))

def show_geo(data):
    if data:
        for i in data:
            geo = str(i.get('geoinfo'))
            spgeo = geo.split()
            spgeovalue = (spgeo[12])
            geoarr.append(spgeovalue)
            #print(i.get('site'), i.get('ip'))
            #print(i.get('geoinfo'))



def show_ip_port(data):
    if data:
        for i in data:
            print(i.get('ip'), i.get('portinfo').get('port'))


def zoomeye_api_test():
    zoomeye = ZoomEye()
    #zoomeye.username = raw_input('ZoomEye Username: ')
    zoomeye.username = 'teknicalmagetwitch@gmail.com'
    zoomeye.password = 'Arkamides1678!'
    #zoomeye.password = getpass.getpass(prompt='ZoomEye Password: ')
    zoomeye.login()
    print(zoomeye.resources_info())

    #pagenum = 1
    #data = zoomeye.dork_search('"ZTE ZXV10 W300" Shopify')
    #show_site_ip(data)

    time.sleep(1)
    print("|___________________|")

      
    country_code =  ("country:'RU'")
    query = "Shopify"
    #app = 'app:"ZTE ZXV10 W300 ADSL router http config"'
    dork = (query + ' '+ country_code)
    print(dork)
    


    x = 1
    while x < 5:   
        
        
        data = zoomeye.dork_search('Shopify', page=x, facet=['not ip'])

        #data = zoomeye.dork_search(dork, page=x, facet=['not ip'])
        show_site_ip(data)
        show_geo(data)

        print("---")
        
        #print(geoarr)
        #print(show_site_ip(data))
        #geo2 = str(show_geo(data))
        #geo3 = geo2.split()
        #print(geo3[12])
        x+=1
        print(x)
        print("___________________")

    print(iparr)
    print('Trash')
    print(geoarr)

    #data = zoomeye.dork_search('country:cn')
    #show_site_ip(data)

    #data = zoomeye.dork_search('solr country:cn')
    #show_site_ip(data)

    #data = zoomeye.dork_search('solr country:cn', resource='host')
    #show_ip_port(data)


if __name__ == "__main__":
    zoomeye_api_test()
