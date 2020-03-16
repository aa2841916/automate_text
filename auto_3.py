from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class Solution:
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
        # self.brower.maximize_window()
        element = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id('kw'))

        element.send_keys('selenium')

        driver.implicitly_wait(30)
        driver.find_element_by_id('su').click()
        time.sleep(5)
        driver.quit()





