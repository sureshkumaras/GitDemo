from selenium.webdriver.common.by import By

from pageobject.checkout_confirmation import CheckoutConfirmation
from utils.browser_utils import BrowserUtils


class ShopPage(BrowserUtils) :

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, " a[href*='shop']")
        self.products_cart = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_product_to_cart(self, product_name):
        #  //a[contains(@href,'shop')]    a[href*='shop']
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.products_cart)

        for product in products:
            product_names = product.find_element(By.XPATH, "div/h4/a").text
            if product_names == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = CheckoutConfirmation(self.driver)
        return checkout_confirmation