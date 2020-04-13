from selenium import webdriver
import time
class Solution:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('肥肥的囧哥')
        self.driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys('2841916')
        self.driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
        time.sleep(3)

        self.driver.quit()




if __name__ == '__main__':
    Solution()