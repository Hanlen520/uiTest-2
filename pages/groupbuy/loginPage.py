#coding=utf-8
'''封装团购登陆页面类'''
from common import basePage
from allure import MASTER_HELPER
from selenium import webdriver

'''基于PageObject模式,定义页面类，继承基类'''
class LoginPage(basePage.BasePage):


    '''相关元素'''
    url="https://www.djcps.com/login.html"
    username=("id","username")
    password=("id","password")
    login_button=("id","login-button")

    '''封装登陆方法'''
    @MASTER_HELPER.step("登陆团购系统")
    def login(self,username,password):
        '''访问网址，输入账号密码，点击登录按钮'''
        self.get(url=self.url)
        self.sendKeys(self.username,text=username)
        self.sendKeys(self.password,text=password)
        self.click(self.login_button)

'''测试'''
if __name__ == '__main__':
    driver=webdriver.Chrome()
    page=LoginPage(driver)
    page.login("17826826147","zyk123456")