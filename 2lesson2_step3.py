from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select 

def calc(x,y):
    return str(int(x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    z = calc(x,y)

    select = Select(browser.find_element(By.TAG_NAME, "select")) 
    select.select_by_value(z) 

    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()

