import pickle
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def LoadPage():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    landing = 'https://www.quora.com/What-s-something-that-you-noticed-when-you-quit-a-bad-habit/log'

    driver.get(landing)

    


            

    print('exit_key')
    #f_text = open('text.txt', 'w')
    #f_author = open('Author.txt', 'w')

    cnt = 1
    while cnt < 1000000:    
        
        #x = driver.find_elements_by_xpath('//*[@class="q-box qu-cursor--pointer qu-hover--textDecoration--underline"]')[cnt].click()

        z = driver.find_elements_by_xpath('//*[@class="q-box qu-cursor--pointer qu-hover--textDecoration--underline"]')[cnt].get_attribute('href')

        #time.sleep(5)

        #driver.get(landing)

        print(z)
        
        time.sleep(.5)

        cnt+=2
            
    #!
           
                
                
        

                
    print("L")
    time.sleep(500) 

LoadPage()

    


