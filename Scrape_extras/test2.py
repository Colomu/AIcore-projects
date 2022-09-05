from tracemalloc import start
from selenium import webdriver
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

import os



from Scraper.Scraper.constants import BASE_URL
print('start')

class scraper:
    def __init__(self):
        self.driver_path = "/Users/charlesolomu/Documents/chromedriver"
        self.service = Service(self.driver_path)
        self.URL = BASE_URL
        chrome_options = Options()
        self.driver = webdriver.Chrome(self.driver_path, options=chrome_options)

    def land_first_page(self):
        self.driver.get(self.URL)

if __name__ == "__main__":
    print('start')
    bot = scraper()
    bot.land_first_page()
    time.sleep(5)

    def click_element(self, xpath: str):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
