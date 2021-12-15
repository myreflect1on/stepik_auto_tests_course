from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_css_selector("div.first_block &gt; div.first_class &gt; input")
    input1.send_keys("First")
    input2 = browser.find_element_by_css_selector("div.first_block &gt; div.second_class &gt; input")
    input2.send_keys("Second")
    input3 = browser.find_element_by_css_selector("div.first_block &gt; div.third_class &gt; input")
    input3.send_keys("Third")

    button = browser.find_element_by_css_selector(".btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()