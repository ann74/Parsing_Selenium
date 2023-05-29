# Открываем http://parsinger.ru/selenium/7/7.html с помощью selenium;
# Получаем значения всех элементов выпадающего списка;
# Суммируем(плюсуем) все значения;
# Вставляем получившийся результат в поле на сайте;
# Нажимаем кнопку и копируем длинное число;

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/7/7.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    num = sum(int(elem.text) for elem in browser.find_elements(By.TAG_NAME, 'option'))
    browser.find_element(By.ID, 'input_result').send_keys(num)
    browser.find_element(By.ID, 'sendbutton').click()
    time.sleep(1)
    print(browser.find_element(By.ID, 'result').text)
