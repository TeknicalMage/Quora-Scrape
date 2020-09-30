import time
import random
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import pickle


def LoadPage():

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.google.com/search?sxsrf=ALeKk021OgtqJkVUo0VFjHIq_y8v1n_K9g%3A1601419423061&source=hp&ei=nrhzX_fRPMOFytMP-82T2AY&q=dumb&oq=dumb&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIHCC4QsQMQQzIECAAQQzIFCAAQsQMyBAgAEEMyAggAMgQIABBDMgcILhCxAxBDMggILhDHARCvATIICC4QxwEQrwE6BAgjECc6BQgAEJECOggILhCxAxCDAToLCC4QsQMQxwEQowI6CAgAELEDEIMBOgkIIxAnEEYQ-QE6CAgAELEDEJECOgUILhCxA1CyBljoCmDHC2gAcAB4AIABowGIAZ4DkgEDMC4zmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwj3mOCeuI_sAhXDgnIEHfvmBGsQ4dUDCAk&uact=5')
    x = 0
    while 1:
        
        print(z)
        x+=1

    

LoadPage()

    


