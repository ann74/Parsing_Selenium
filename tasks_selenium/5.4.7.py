# Открыть http://parsinger.ru/selenium/1/1.html с помощью selenium;
# Заполнить все существующие поля;
# Нажмите на кнопку;
# Скопируйте результат который появится рядом с кнопкой в случае если вы уложились в 5 секунд;

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/1/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    inputs = browser.find_elements(By.CLASS_NAME, 'form')
    for input_ in inputs:
        input_.send_keys('text')
    browser.find_element(By.ID, 'btn').click()
    time.sleep(2)
    print(browser.find_element(By.ID, 'result').text)
