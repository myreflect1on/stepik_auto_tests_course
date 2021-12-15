from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    num1 = int(browser.find_element_by_id("num1").text)
    print(num1)
    num2 = int(browser.find_element_by_id("num2").text)
    print(num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(num1+num2))  # ищем элемент с текстом "Python"
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла