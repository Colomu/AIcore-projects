from selenium import webdriver
import pandas as pd
web = "https://www.audible.com/search?keywords=landslide&ref-override=a_search_t1_header_search&k=landslide&crid=1O6FXIEGVYH3T&sprefix=landslide%2Cna-audible-us%2C166&i=na-audible-us&url=search-alias%3Dna-audible-us&ref=nb_sb_noss_1"
path = "/Users/charlesolomu/Documents/chromedriver"
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

container = driver.find_element_by_class_name('adbl-impression-container')
products = container.find_elements_by_xpath('./li')

book_title = []
book_author =[]
book_length = []

for product in products:
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)
    

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)    
print(df_books)
    

'//a[@class="call"])':

def accept_cookies(self, XPATH: str = 
        '''
        Finds and clicks the "Accept" cookies button.

        parameters
        '''''''
        xpath: str
            The Xpath of the accept cookies button

        '''''''''
        accept_cookies = bot.driver.find_element(By.XPATH)         
        accept_cookies.click()
        time.sleep(5)

    def elements_in_container(self, plasma_stds, XPATH_container, tag_elements) -> list:

        plasma_stds =  bot.driver.find_element(By.XPATH, '//*[@id="145ba1e5c66944848c66caa51c19cdbc"]/div/div[2]/div/div[1]/a')
    
        container = bot.driver.find_element(By.XPATH, '//*[@id="plasma"]')
    
        elements_in_container = container.find_elements(By.XPATH, '.tr')def accept_cookies(self, XPATH: str = '//a[@class="call"])':

        '''
        Finds and clicks the "Accept" cookies button.

        parameters
        '''''''
        xpath: str
            The Xpath of the accept cookies button

        '''''''''
        accept_cookies = bot.driver.find_element(By.XPATH)         
        accept_cookies.click()
        time.sleep(5)

    def elements_in_container(self, plasma_stds, XPATH_container, tag_elements) -> list:

        plasma_stds =  bot.driver.find_element(By.XPATH, '//*[@id="145ba1e5c66944848c66caa51c19cdbc"]/div/div[2]/div/div[1]/a')
    
        container = bot.driver.find_element(By.XPATH, '//*[@id="plasma"]')
    
        elements_in_container = container.find_elements(By.XPATH, '.tr')



        