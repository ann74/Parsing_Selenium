# Откройте http://parsinger.ru/selenium/3/3.html;
# Извлеките данные из каждого тега <p>;
# Сложите все значения, их всего 300 шт;
# Напишите получившийся результат в поле ниже

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    res = sum(int(elem.text) for elem in browser.find_elements(By.TAG_NAME, 'p'))
    time.sleep(2)
    print(res)
