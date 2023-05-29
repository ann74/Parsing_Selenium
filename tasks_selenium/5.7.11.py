# У вас есть список сайтов, 6 шт;
# На каждом сайте есть chekbox, нажав на этот chekbox появится код;
# Ваша задача написать скрипт, который открывает при помощи Selenium все сайты во вкладках (.window_handles);
# Проходит в цикле по каждой вкладке, нажимает на chekbox и сохранеят код;
# Из каждого числа, необходимо извлечь корень, функцией sqrt();
# Суммировать получившиеся корни и вставить результат в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
with webdriver.Chrome() as browser:
    res = 0
    for site in sites:
        browser.execute_script(f'window.open("{site}", "_blank");')
        browser.switch_to.window(browser.window_handles[1])
        browser.find_element(By.CSS_SELECTOR, 'input[class="checkbox_class"]').click()
        res += int(browser.find_element(By.ID, 'result').text) ** 0.5
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    print(round(res, 9))
