from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, "book")

    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))

    button.click()

    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # Переводит функцию в текст и передает на ввода в поле ввода
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    print(y)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    buttonsubmit = browser.find_element(By.ID, "solve")
    buttonsubmit.click()

finally:
    time.sleep(15)

    browser.quit()