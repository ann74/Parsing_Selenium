# Откройте http://parsinger.ru/scroll/4/index.html с помощью Selenium;
# На сайте есть 50 кнопок, которые визуально перекрыты блоками;
# После нажатия на кнопку в id="result" появляется уникальное для каждой кнопки число;
# Цель: написать скрипт, который нажимает поочерёдно все кнопки и собирает уникальные числа;
# Все полученные числа суммировать, и вставить результат в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/scroll/4/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    res = 0
    for elem in browser.find_elements(By.CLASS_NAME, 'btn'):
        browser.execute_script("return arguments[0].scrollIntoView(true);", elem)
        elem.click()
        res += int(browser.find_element(By.ID, 'result').text)
    print(res)
