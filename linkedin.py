# # Selenium imports here
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait

# # Other imports here
# import os
# import wget
# import time

# driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver')
# driver.get('https://www.linkedin.com/')

# # Find the login input fields and enter the username and password
# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))
# username.clear()
# password.clear()
# username.send_keys("noone_21502")
# password.send_keys("noone5757")

# # Find the login button and click it
# login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
# login_button.click()

# # Wait for some time to let the page load
# time.sleep(5)

# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))
# username.clear()
# password.clear()
# username.send_keys("psthakkar2@gmail.com")
# password.send_keys("parth@5757")

# # Find the login button and click it
# login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
# login_button.click()

# # Wait for some time to let the page load
# time.sleep(5)

# # Close the driver
# # Wait for the user to press the 'q' key to quit
# while True:
#     key = input("Press 'q' to quit: ")
#     if key.lower() == 'q':
#         driver.quit()
#         break


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time

driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver')
driver.get('https://www.linkedin.com/')

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))
username.clear()
password.clear()
username.send_keys("noone_21502")
password.send_keys("noone5757")

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login_button.click()

time.sleep(5)

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))
username.clear()
password.clear()
username.send_keys("psthakkar2@gmail.com")
password.send_keys("parth@5757")
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login_button.click()
time.sleep(5)
work_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-item__work")))
work_button.click()
my_company_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='app-aware-link global-nav__primary-link--active global-nav__primary-link hyperlink']")))
my_company_button.click()
time.sleep(5)
while True:
    key = input("Press 'q' to quit: ")
    if key.lower() == 'q':
        driver.quit()
    break

