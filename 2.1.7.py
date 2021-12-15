from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    treasure = browser.find_element_by_id("treasure")
    print(treasure)
    valuex = treasure.get_attribute("valuex")
    print(valuex)
    x = valuex
    y = math.log((abs(12 * math.sin(int(x)))))
    print(y)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(y))
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    robotCheckbox.click()
    robotsRule = browser.find_element_by_id('robotsRule')
    robotsRule.click()
    time.sleep(3)
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла