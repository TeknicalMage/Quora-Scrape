import pickle
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

landing = 'https://www.quora.com/What-s-something-that-you-noticed-when-you-quit-a-bad-habit/log'


def LoadPage():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(landing)


    while 1:
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
        #f_text = open('text.txt', 'w')
        #f_author = open('Author.txt', 'w')
        time.sleep(10)
        cnt = 1
        while cnt < 1000000:
    
            z = driver.find_elements_by_xpath('//*[@class="q-box qu-cursor--pointer qu-hover--textDecoration--underline"]')[cnt].get_attribute('href')

            #time.sleep(5)

            #driver.get(landing)

            print(z)
        
            time.sleep(.5)

            cnt+=2

        
                
            
        

                
        print("L")
        time.sleep(500) 

LoadPage()

    


