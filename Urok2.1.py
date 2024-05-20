from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://suninjuly.github.io/math.html"
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
#Вписываем в поле ввода
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
#Выбираем чек бокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
#Ставит флаг на радиохеде
    radio = browser.find_element(By.CSS_SELECTOR, "[for=robotsRule]")
    radio.click()
#Нажимаем на кнопку
    button_submit = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button_submit.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()