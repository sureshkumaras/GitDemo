from selenium.webdriver.common.by import By

from pageobject.shop import ShopPage
from utils.browser_utils import BrowserUtils


class LoginPage(BrowserUtils) :

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input ).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shop_page = ShopPage(self.driver)
        print("======== master code")
        print("======== iam in develop branch")
        print("======== develop branch completely developed 2nd line")
        return shop_page

    @staticmethod
    def check_check():
        print("====== check")

