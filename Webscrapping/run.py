from Scraper.Scraper.Scraper import scraper
import time

if __name__ == "__main__":
    print('start')
    bot = scraper()
    bot.land_first_page()
    time.sleep(5)
    bot.accept_cookies
    time.sleep(5)