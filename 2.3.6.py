from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    button1= browser.find_element_by_xpath('//button[contains(text(), "I want to go on a magical journey!")]')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input_value = browser.find_element_by_id('input_value') # input_value
    x = input_value.text
    y = math.log((abs(12 * math.sin(int(x)))))
    print(y)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(y))

    time.sleep(1)
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла