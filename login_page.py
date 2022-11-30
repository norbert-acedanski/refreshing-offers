class LoginSprzedajemy:
    textbox_email_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"
    button_login_xpath = "//button[@type='submit']"
    button_logout_xpath = "//a[@class='logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()


class MyOffersSprzedajemy:
    button_cookies_xpath = "//button [@id='didomi-notice-agree-button']"
    button_next_page_xpath = "//li[@class='next']"
    number_of_pages_xpath = "//ul[@class='cntPaginator'] /li[last() - 1] //span"
    number_of_offers_in_a_page = "//input[@name='limit']"
    checkbox_check_all_xpath = "//a[@class='selectDeselectAll'] /span"
    button_refresh_xpath = "//div[@class='theButton theButtonNoBg theButtonRefresh'] /a"

    def __init__(self, driver):
        self.driver = driver
    
    def agree_to_cookies(self):
        self.driver.find_element_by_xpath(self.button_cookies_xpath).click()

    def find_number_of_pages(self):
        return int(self.driver.find_element_by_xpath(self.number_of_pages_xpath).text)

    def check_all_offers(self):
        self.driver.find_element_by_xpath(self.checkbox_check_all_xpath).click()

    def refresh_offers(self):
        self.driver.find_element_by_xpath(self.button_refresh_xpath).click()
    
    def go_to_next_page(self):
        self.driver.find_element_by_xpath(self.button_next_page_xpath).click()