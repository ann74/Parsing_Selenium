# Откройте http://parsinger.ru/scroll/3/ с помощью Selenium;
# Ваша задача, получить числовое значение  id="число" с каждого тега <input> который при нажатии вернул число;
# Суммируйте все значения и отправьте результат в поле ниже.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


url = 'http://parsinger.ru/scroll/3/'
with webdriver.Chrome() as browser:
    browser.get(url)
    res = 0
    for item in browser.find_elements(By.CLASS_NAME, 'item'):
        input_tag = item.find_element(By.TAG_NAME, 'input')
        input_tag.send_keys(Keys.DOWN)
        input_tag.click()
        number = item.find_element(By.TAG_NAME, 'span').text
        if number:
            res += int(input_tag.get_attribute("id"))
    print(res)
