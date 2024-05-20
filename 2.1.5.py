from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
#Функция
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
#Переводит функцию в текст и передает на ввода в поле ввода
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    print(y)
#поле ввода
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
# Скролл страницы.
    checkbox = browser.find_element(By.ID,"robotCheckbox")
    checkbox.click()

    radihead = browser.find_element(By.ID, "robotsRule")
    radihead.click()

    button.click()



finally:
    time.sleep(5)

    browser.quit()