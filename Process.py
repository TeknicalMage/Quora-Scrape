import pickle
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import csv

import Parserman as PM



fml = open('sample.csv','a')
writer = csv.writer(fml)




def LoadPage():
    print('Made by TekMage')
    print('Please Copy and paste the Quora Log Link below')
    zxy = askme()

    print(zxy)

    landing = zxy
    time.sleep(2)


    chrome_options = Options()

    chrome_options.add_argument('--user-data-dir=C:/Users/arcaz/Documents/ChromeDev1/User Data')

    chrome_options.add_argument('--profile-directory=Profile 1')
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(landing)

    yee = 68
    while yee == 68:
        SCROLL_PAUSE_TIME = 0.3

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while 1:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            #print(last_height)
            #print (new_height) 
            

        print('exit_key')
        f = open('Names.txt', 'w')
        writer.writerow(['Links', 'Views', 'Followers', 'Last Accessed', 'Cateogory'])

        #f_author = open('Author.txt', 'w')
        time.sleep(1)
        cnt = 1
        try:
            while cnt < 1000000:
        
                z = driver.find_elements_by_xpath('//*[@class="q-box qu-cursor--pointer qu-hover--textDecoration--underline"]')[cnt].get_attribute('href')
                

                #time.sleep(5)

                #driver.get(landing)

                print(z)
                f.write(z + "\n")
            
                cnt+=2
        except:
            pass

        #print(PM.ayok())

  
        print("SECOND STAGE TIMMMMMMMMEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        break

    t = PM.ayok()

       
    for i in t: 
        print(i) 
        driver.get(i)
        time.sleep(1)

        

        try:
            try:
                views = driver.find_element_by_xpath('//*[@class="CssComponent-sc-1oskqb9-0 AbstractSeparatedItems___StyledCssComponent-sc-46kfvf-0 bxBZxD"]').get_attribute('innerText')
                px = str(views)
            except:
                px = '0 views/Deleted'

            try:
                date = driver.find_element_by_xpath('//*[@class="q-text qu-color--gray qu-fontSize--small qu-passColorToLinks qu-truncateLines--1"]').get_attribute('innerText')
                pz = str(date)
            except:
                pz = 'Deleted or NA Date'

            try:
                follower = driver.find_element_by_xpath('//*[@style="box-sizing: border-box; direction: ltr; position: relative; height: 18px; flex-shrink: 0;"]').get_attribute('innerText')
                py = str(follower)
            except:
                py = str(0)   #Followers Count ^^

            #Catogory
            pw = driver.find_elements_by_xpath('//*[@style="background: none;"]')[0].get_attribute('innerText')


            l_link = []
            l_view = []
            l_follower = []
            l_date = []
            l_cateogory = []

            el_l = [l_view, l_follower, l_date]
                  

            l_link.append(i)

            #print(px) 
            l_view.append(px) 
            
            #print(py + " FOLLOWERS")
            l_follower.append(py)      
            
            #print(pz)
            l_date.append(pz)

            #print(pw)
            l_cateogory.append(pw)

            time.sleep(.05)
            #print(el_l)
            writer.writerow([l_link, l_view, l_follower, l_date, l_cateogory])
            #row = 'x'
        except:
            pass
        
    
    print('File Written')



def askme():
    site = input()
    return site


    
LoadPage()

    


