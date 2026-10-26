import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
##########################
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#====================================adding items to cart================================================
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4) ######### -> exceptional for this condition
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))
assert len(results) > 0
#--------------------------- get products names
product_names = []
expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
for result in results:
    result.find_element(By.XPATH,"div/button").click()
    product_names.append(result.find_element(By.XPATH, "h4").text)
#------------------------- compare products present

assert sorted(product_names) == sorted(expected_list)

print(product_names)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#=================================calculate sum===================================================
prices = driver.find_elements(By.XPATH,"//tbody/tr/td[5]/p")
total=0
for price in prices:
    total=total+int(price.text)

#=======================================apply promocode=============================================
#time.sleep(4)
promocode = "rahulshettyacademy"
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys(promocode)
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
#time.sleep(6)
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
message = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
print(message)
#======================================assert sum & total value, discount total============================

totalsum = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(totalsum)
assert total==totalsum
discount_total = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print("============"+discount_total)
assert totalsum > discount_total
#====================================================================================
time.sleep(20)
