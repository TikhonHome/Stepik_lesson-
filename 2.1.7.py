from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    print(y)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    # Ставит флаг на радиохеде
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    # Нажимаем на кнопку
    button_submit = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button_submit.click()

finally:
    time.sleep(10)


    browser.quit()