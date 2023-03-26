import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--no-gpu')
chrome_options.add_argument('--disable-setuid-sandbox')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options = chrome_options)

# login
driver.get('https://app.gptzero.me/login')
WebDriverWait(driver, 50, 0.5).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Login"]')))
email_element = driver.find_element(By.XPATH, '//input[@type="emailId"]')
email_element.clear()
email_element.send_keys('hwtthyz@126.com')
passwd_element = driver.find_element(By.XPATH, '//input[@type="password"]')
passwd_element.clear()
passwd_element.send_keys('meta2023')
login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
login_button.click()
WebDriverWait(driver, 100, 0.5).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Continue Free"]')))
continue_button = driver.find_element(By.XPATH, '//a[text()="Continue Free"]')
continue_button.click()

# get elements
WebDriverWait(driver, 100, 0.5).until(EC.presence_of_element_located((By.NAME, 'textarea1')))
textarea_element = driver.find_element(By.NAME, 'textarea1')
agree_checkbox_element = driver.find_element(By.NAME, 'checkbox1')
agree_checkbox_element.click()
get_result_element = driver.find_element(By.XPATH, '//button[text()="Get Results"]')

# input texts
text = 'Yesterday I went to school and I was very happy to see my friends. We played basketball for one and a half hours and played soccer for another two hours. My friends said I was one of the best basketball player in the school. I was very happy. After school we went to have dinner.'
assert(len(text) >= 250)
textarea_element.clear()
textarea_element.send_keys(text)
get_result_element.click()
try:
    WebDriverWait(driver, 100, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'py-4')))
    result_head_element = driver.find_element(By.CLASS_NAME, 'py-4')
    print(result_head_element.text)
except:
    pass


