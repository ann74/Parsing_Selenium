# Откройте http://parsinger.ru/selenium/6/6.html при помощи selenium;
# Найдите значение выражения на странице;
# Найдите и выберите в  выпадающем списке элемент с числом, которое у вас получилось после нахождения значения уравнения;
# Нажмите на кнопку;
# Скопируйте число и вставьте в поле ответа.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/6/6.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    result = (eval((browser.find_element(By.ID, 'text_box')).text))
    nums = browser.find_elements(By.TAG_NAME, 'option')
    for num in nums:
        if int(num.text) == result:
            num.click()
            break
    browser.find_element(By.ID, 'sendbutton').click()
    time.sleep(2)
    print(browser.find_element(By.ID, 'result').text)
