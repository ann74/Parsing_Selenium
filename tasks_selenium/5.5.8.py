# Откройте https://parsinger.ru/methods/5/index.html с помощью Selenium;
# На сайте есть 42 ссылки, у каждого сайта по ссылке есть cookie с определёнными сроком жизни;
# Цель: написать скрипт, который сможет найти среди всех ссылок страницу с самым длинным сроком жизни cookie и получить
# с этой страницы число;

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/methods/5/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    max_expiry = 0
    res = 0
    for link in browser.find_elements(By.CLASS_NAME, 'urls'):
        link.click()
        expiry = int(browser.get_cookie('foo2')['expiry'])
        if expiry > max_expiry:
            max_expiry = expiry
            res = browser.find_element(By.ID, 'result').text
        browser.back()
    print(res)
