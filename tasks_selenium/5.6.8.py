# Откройте http://parsinger.ru/scroll/2/index.html с помощью Selenium;
# На сайте есть 100 чекбоксов, 25 из них вернут число;
# Ваша задача суммировать все появившиеся числа;
# Отправить получившийся результат в поля ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


url = 'http://parsinger.ru/scroll/2/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    res = 0
    for item in browser.find_elements(By.CLASS_NAME, 'item'):
        input_tag = item.find_element(By.TAG_NAME, 'input')
        input_tag.send_keys(Keys.DOWN)
        input_tag.click()
        number = item.find_element(By.TAG_NAME, 'span').text
        if number:
            res += int(number)
    print(res)
