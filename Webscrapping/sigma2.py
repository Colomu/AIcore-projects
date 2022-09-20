from tkinter import Frame
from tracemalloc import start
from selenium import webdriver
import selenium
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from typing import List

import os
import logging



from Scraper.Scraper.constant2 import BASE_URL
print('start')

class Scraper:
    def __init__(self):
        self.driver_path = "/Users/charlesolomu/Documents/chromedriver"
        self.service = Service(executable_path=self.driver_path)
        
        self.URL = BASE_URL
        chrome_options = Options()
        self.driver = webdriver.Chrome(self.driver_path, options=chrome_options)

    def land_first_page(self):
        self.driver.get(self.URL)

    

    def click_element(self, xpath: str):
        element = self.driver.find_element(By.XPATH, xpath)
        #element = self.driver.switch_to.active_element
        element.click()
        '''fd
        i89\'HJNM  u
        Finds and clicks an element in the website
        parameters
        '''''''
        xpath: str
            The Xpath of the element button

        '''''''''
    
    
    def accept_cookies(self, xpath: str = '//button[@id="onetrust-accept-btn-handler"]'):
        '''
        Finds and clicks the "Accept" cookies button.

        parameters
        '''''''
        xpath: str
            The Xpath of the accept cookies button

        '''''''''
    
    
       
        #self.driver.switch_to.frame(2) 
        
        
        self.click_element(xpath)
    
    

class Thermoscraper(Scraper):
    def applications_techniques_chemicals(self, xpath: str):
        self.accept_cookies()
        time.sleep(1)
        self.click_element(xpath)
        chemicals=self.find_elements(By.xpath)

    
#(//a[@href="/uk/en/home/chemicals.html"])[2]

if __name__ == "__main__":
    print('start')
    bot = Scraper()
    bot.land_first_page()
    time.sleep(3)
    bot.accept_cookies()
    WindowH = bot.driver.window_handles[0]
    time.sleep(2)

    #bot = Scraper()
    #bot.driver.switch_to.default_content()
    bot.driver.switch_to.window(WindowH)
    time.sleep(3)
    #logging.error(bot.driver.switch_to.active_element)
    bot.click_element('(//a[@href="/GB/en/life-science/vaccine-development-and-manufacturing"])[2]')
    time.sleep(3)
