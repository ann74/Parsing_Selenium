# Откройте https://parsinger.ru/methods/3/index.html с помощью Selenium;
# Ваша задача получить все значения cookie с чётным числом после "_" и суммировать их;

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/methods/3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    cookies = browser.get_cookies()
    res = sum(int(cookie['value']) for cookie in cookies if not int(cookie['name'][-1]) % 2)
    print(res)
