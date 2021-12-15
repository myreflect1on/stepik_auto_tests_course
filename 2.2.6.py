from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    input_value = browser.find_element_by_id('input_value') # input_value
    x = input_value.text
    y = math.log((abs(12 * math.sin(int(x)))))
    print(y)

    answer = browser.find_element_by_id('answer')
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    robotsRule = browser.find_element_by_id('robotsRule')
    button = browser.find_element_by_tag_name("button")

    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(str(y))
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    robotCheckbox.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)


    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла