import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
        self.assertEqual(abs(42), 42, "http://suninjuly.github.io/registration1.html is not ok")

        # не забываем оставить пустую строку в конце файла

    def test_registration1(self):

        link = "http://suninjuly.github.io/registration1.html"
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
        self.assertEqual(abs(42), 42, "http://suninjuly.github.io/registration2.html is not ok")

        # не забываем оставить пустую строку в конце файла
if __name__ == "__main__":
    unittest.main()



