# Открываем http://parsinger.ru/selenium/2/2.html при помощи selenium;
# Применяем метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT;
# Кликаем по ссылке с текстом 16243162441624;
# Результат будет ждать вас в теге <p id="result"></p>  ;
# Скопируйте найденный результат в поле ниже.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/2/2.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    browser.find_element(By.LINK_TEXT, '16243162441624').click()
    time.sleep(2)
    print(browser.find_element(By.ID, 'result').text)
