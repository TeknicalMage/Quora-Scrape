import pickle
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



landing = 'https://www.quora.com/What-s-something-that-you-noticed-when-you-quit-a-bad-habit/answer/Stephen-J-Lalla'
landing2 = 'https://www.quora.com/What-s-something-that-you-noticed-when-you-quit-a-bad-habit/answer/Catherine-Leowlc'


def LoadPage():
    chrome_options = Options()

    chrome_options.add_argument('--user-data-dir=C:/Users/arcaz/Documents/ChromeDev1/User Data')

    chrome_options.add_argument('--profile-directory=Profile 1')

    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(landing2)

    pw = driver.find_elements_by_xpath('//*[@style="background: none;"]')[1].get_attribute('innerText')
    print(pw)

    #Text
    

LoadPage()

    


