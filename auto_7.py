from selenium import webdriver
import time

class Solution():
    def __init__(self,url):
        """

        :param url: 测试地址
        """
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

        nowhandle = self.driver.current_window_handle

        # self.driver.find_element_by_partial_link_text('登录').click()

        self.driver.get(url)



        time.sleep(5)

        self.driver.quit()

if __name__ == '__main__':
    solution = Solution('https://passport.baidu.com/v2/?reg&tt=1586242988659&overseas=undefined&gid=49921E1-7FAA-44C9-B8CE-5635D09BFB91&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2F')
    solution.driver