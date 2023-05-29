# Откройте https://parsinger.ru/methods/3/index.html с помощью Selenium;
# На сайте есть определённое количество секретных cookie;
# Ваша задача получить все значения и суммировать их;

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/methods/3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    cookies = browser.get_cookies()
    res = sum(int(cookie['value']) for cookie in cookies)
    print(res)
