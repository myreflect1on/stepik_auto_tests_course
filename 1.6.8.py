from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_tag_name('[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_tag_name('[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_tag_name('[placeholder="Input your email"]')
    input3.send_keys("Smolensk@mail.ru")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла