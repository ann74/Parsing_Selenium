# Откройте http://parsinger.ru/infiniti_scroll_2/ с помощью Selenium;
# На сайте есть список из 100 элементов, которые генерируются при скроллинге;
# Необходимо прокрутить окно в самый низ;
# Цель: получить все значение в элементах, сложить их;

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


url = 'http://parsinger.ru/infiniti_scroll_2/'
with webdriver.Chrome() as browser:
    browser.get(url)
    res = 0
    list_input = set()
    flag = False
    while True:
        items = [x for x in browser.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, "p")]
        for item in items:
            if item not in list_input:
                tag_input = item.find_element(By.TAG_NAME, 'input')
                tag_input.send_keys(Keys.DOWN)
                tag_input.click()
                res += int(item.text)
                time.sleep(1)
                list_input.add(item)
            if item.get_attribute('class') == 'last-of-list':
                flag = True
                break
        if flag:
            break
    print(res)
