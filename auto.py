from selenium import webdriver
import time
class Solution:
    def __init__(self,url):
        """

        :param url: 测试地址
        """
        # self.brower = webdriver.Chrome()
        # self.brower.get(url)
        # print('像素化')
        # self.brower.set_window_size(480,800)
        # time.sleep(3)
        # self.brower.quit()

        # first_url = 'http://www.baidu.com'
        # second_url = 'http://news.baidu.com'
        # self.brower = webdriver.Chrome()
        # self.brower.get(first_url)
        # self.brower.get(second_url)
        # self.brower.back()
        # first = print('后退到首页，地址是：' + first_url)
        # time.sleep(3)
        # self.brower.forward()
        # second = print('前进到首页，地址是：' + second_url)
        # self.brower.quit()






solution = Solution('http://m.mail.10086.cn')
solution.brower
