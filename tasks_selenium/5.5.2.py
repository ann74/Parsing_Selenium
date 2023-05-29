# Откройте https://parsinger.ru/methods/1/index.html с помощью Selenium;
# При обновлении сайта, в id="result" появится число;
# Обновить страницу возможно придется много раз, т.к. число появляется не часто;
# Вставьте полученный результат в поле для ответа:

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/methods/1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    res = browser.find_element(By.ID, 'result').text
    while not res.isdigit():
        browser.refresh()
        res = browser.find_element(By.ID, 'result').text
    print(res)
