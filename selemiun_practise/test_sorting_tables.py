import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_sort(browser_instance) :
    driver = browser_instance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    browser_sorted_veggies = []
    driver.find_element(By.XPATH, "//th[@role='columnheader'][1]/span[1]").click()
    names_list = driver.find_elements(By.XPATH, "//tr/td[1]")
    for name in names_list:
        browser_sorted_veggies.append(name.text)

    browser_sorted_veggies_list = browser_sorted_veggies.copy()

    assert sorted( browser_sorted_veggies_list) == browser_sorted_veggies

