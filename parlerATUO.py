import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys





def AHHHHHHHHHHHHHH():
 
    landing = 'https://parler.com/feed'
    keyword = 'dog'
    time.sleep(2)


    chrome_options = Options()

    chrome_options.add_argument('--user-data-dir=C:/Users/arcaz/Documents/ChromeDev/User Data')
    chrome_options.add_argument('--profile-directory=Profile 2')
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(landing)
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(keyword)

    time.sleep(1)

    #print(x)

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


    time.sleep(45)



AHHHHHHHHHHHHHH()

    


