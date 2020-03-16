from selenium import webdriver
import os
from time import sleep

class Solution():
    def __init__(self):
        self.driver = webdriver.Chrome()
        file_path = 'file:///' + os.path.abspath('frame.html')
        self.driver.get(file_path)
        self.driver.implicitly_wait(30)

        self.driver.switch_to.frame('f1')
        self.driver.switch_to.frame('f2')

        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id('su').click()

        sleep(5)

        self.driver.quit()


Solution().driver
