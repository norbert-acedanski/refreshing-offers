from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException

from login_page import LoginSprzedajemy, MyOffersSprzedajemy
from getpass import getpass
import time


class RefreshingSprzedajemy():
    sprzedajemy_url = "https://sprzedajemy.pl/Twoje-Oferty"

    def get_credentials(self):
        print("Refreshing sprzedajemy offers")
        self.email = input("Provide your email: ")
        self.password = getpass("Provide your password: ")
    
    def launch_page(self):
        self.driver = webdriver.Chrome("./resources/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.sprzedajemy_url)
        page_title = self.driver.title
        if "Sprzedajemy.pl" not in page_title or "Logowanie do serwisu" not in page_title:
            raise NoSuchWindowException("It appears, that the site is not correct")
    
    def login(self):
        login_page = LoginSprzedajemy(self.driver)
        login_page.set_email(self.email)
        login_page.set_password(self.password)
        login_page.click_login()
        del self.password
        page_title = self.driver.title
        if "Sprzedajemy.pl" not in page_title or "Twoje ogłoszenia" not in page_title:
            raise NoSuchWindowException("It appears, that the site is not correct")
    
    def refresh_offers(self):
        my_offers = MyOffersSprzedajemy(self.driver)
        try:
            my_offers.agree_to_cookies()
        except NoSuchElementException:
            time.sleep(1)
            my_offers.agree_to_cookies()
        number_of_pages = my_offers.find_number_of_pages()
        for page in range(1, number_of_pages + 1):
            my_offers.check_all_offers()
            my_offers.refresh_offers()
            if page != number_of_pages:
                my_offers.go_to_next_page()


def refresh_offers_from_sprzedajemy():
    refreshing_sprzedajemy_offers = RefreshingSprzedajemy()
    refreshing_sprzedajemy_offers.get_credentials()
    refreshing_sprzedajemy_offers.launch_page()
    refreshing_sprzedajemy_offers.login()
    refreshing_sprzedajemy_offers.refresh_offers()
        

if __name__ == "__main__":
    refresh_offers_from_sprzedajemy()