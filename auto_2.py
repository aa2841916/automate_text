#coding=utf-8
from selenium import webdriver
import time
class Solution:
    def __init__(self,url,user_name,passwrod,i):
        """

        :param url: 测试地址
        :param user_name: 账号
        :param passwrod: 密码
        :int i: 次数
        """
        self.brower = webdriver.Chrome()
        self.brower.get(url)
        self.brower.maximize_window()
        self.brower.find_element_by_id('account_id').clear()
        self.brower.find_element_by_id('account_id').send_keys(user_name)
        time.sleep(1)
        self.brower.find_element_by_id('user_pwd1').clear()
        self.brower.find_element_by_id('user_pwd1').send_keys(passwrod)
        time.sleep(1)
        self.brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/form/div[5]/button').click()
        # self.brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/form/div[5]/button').submit()
        time.sleep(5)

        # text = self.brower.find_element_by_xpath('//*[@id="right_items_box"]/ul[1]/li[2]/div/div/span').text
        title = self.brower.title
        now_url = self.brower.current_url


        if title == '外联平台':
            print('第%r次，成功' %i,now_url)
        else:
            print('第%r次，失败' %i,now_url)

        self.brower.quit()









Solution('http://39.108.83.191:45100/deploy-web/#/login','orgine','yuanqi2019',1).brower
Solution('http://39.108.83.191:45100/deploy-web/#/login','orgine','yuanqi2018',2).brower
Solution('http://39.108.83.191:45100/deploy-web/#/login','orgi3ne','yuanqi2019',3).brower
Solution('http://39.108.83.191:45100/deploy-web/#/login','orgi3ne','yuanqi20191',4).brower


