from selenium import webdriver


class Solution:
    def __init__(self,url):
        """

        :param url:测试地址
        """
        self.driver = webdriver.Chrome()
        self.driver.get(url)

