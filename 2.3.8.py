from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)

    text_to_be_present = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), u'$100')
    )
    button1= browser.find_element_by_xpath('//button[contains(text(), "Book")]')
    button1.click()
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