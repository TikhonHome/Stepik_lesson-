from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")

    inputname = browser.find_element(By.NAME, "firstname")
    inputname.send_keys("Name")

    inputlastname = browser.find_element(By.NAME, "lastname")
    inputlastname.send_keys("Фамилия")

    inputemail = browser.find_element(By.NAME, "email")
    inputemail.send_keys("Joq@stepik.robot")

    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    file_path = os.path.join(current_dir, 'file.txt')

    buttonsubmit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    buttonsubmit.click()
finally:
    time.sleep(5)



    browser.quit()