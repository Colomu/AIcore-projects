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



from Scraper.Scraper.constants import BASE_URL
print('start')

class Scraper:
    def __init__(self):
        self.driver_path = "/Users/charlesolomu/Documents/chromedriver"
        self.service = Service(executable_path=self.driver_path)
        
        self.URL = BASE_URL
        chrome_options = Options()
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)

    def land_first_page(self):
        self.driver.get(self.URL)

    

    def accept_cookies(self, xpath: str = '//a[@class="call"]'):
        '''
        Finds and clicks the "Accept" cookies button.

        parameters
        '''''''
        xpath: str
            The Xpath of the accept cookies button

        '''''''''
    
    
       
        self.driver.switch_to.frame(2) 
        
        
        accept_cookies = self.driver.find_element(By.XPATH, xpath)
        accept_cookies.click()

    def application_techniques(self, xpath: str =  '//*[@id="meganav-content"]/li[2]/a/span'):
        application_techniques = button2
        button2 = self.driver.find_element(by=By.XPATH)
        self.accept_cookies()
        time.sleep(1)
        button2.click()
        

    

    def click_element(self, xpath: str):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        '''fd
        i89\'HJNM  u
        Finds and clicks an element in the website
        parameters
        '''''''
        xpath: str
            The Xpath of the element button

        '''''''''

    def find_elements_in_reagents(self, xpath_reagents, tag_elements) -> list:

        reagents =  self.driver.find_elements(By.XPATH, xpath_reagents)
        elements_in_reagents = reagents.find_elements(By.XPATH, f'./{tag_elements}')    

        return elements_in_reagents




   
    
        
        #reagent_search.click()
        time.sleep(1)
        #reagent_search.send_keys(product)


    def search_all_products(self,):
        self.accept_cookies()
        time.sleep(1)
        self.click_element('//a[@href="#plasma"]')
        products = self.find_elements_in_reagents(xpath_reagents='//div[@id="plasma"]',
                                                    tag_elements='tr')
        links = []
        for product in products:
            link = product.find_element(By.XPATH, './a').get_attribute('href')
            links.append(link)
        
        return links

    
    def get_reagent_info(self):
        table = self.driver.find_element(By.XPATH, '(//tr[@data-uw-styling-context="true"])[1]')
        columns = table.find_element(By.XPATH, './tr')
        catalogue = columns[0]
        #data in the catalogue column

        catalogue_number = self.retreive_columns_info(catalogue)
        name = columns[1]

        reagent_name = self.retreive_columns_info(name)

        price = columns[3]


    @staticmethod
    def retreive_columns_info(column):
        rows_container = column.find_element(By.XPATH, './tr')
        rows = rows_container.find_element(by.XPATH, './th')
        data_list = []
        for row in rows:
            data = row.text
            data_list.append(data)

        return data_list

if __name__ == "__main__":
    print('start')
    bot = Scraper()
    bot.land_first_page()
    time.sleep(5)
    bot.accept_cookies()
    time.sleep(5)
    bot.application_techniques()
    time.sleep(3)
    