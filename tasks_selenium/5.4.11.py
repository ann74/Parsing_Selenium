# Откройте http://parsinger.ru/selenium/4/4.html;
# Установите все чек боксы в положение checked при помощи selenium и метода click();
# Когда все чек боксы станут активны, нажмите на кнопку;
# Скопируйте число которое появится на странице;
# Результат появится в <p id="result">Result</p>;

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/4/4.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    boxes = browser.find_elements(By.CLASS_NAME, 'check')
    for box in boxes:
        box.click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(1)
    print(browser.find_element(By.ID, 'result').text)
