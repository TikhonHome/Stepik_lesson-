from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")

    x = int(x_element.text)
    y = int(y_element.text)
    z = str(x + y)

    print(z)

    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(z)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()


finally:
    time.sleep(5)

    browser.quit()