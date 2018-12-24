#coding=utf-8
'''封装主页'''
from common import basePage

class IndexPage(basePage.BasePage):

    '''页面元素'''
    search_input=("id","searchBox")
    search_button=("id","searchImage")

    '''组件'''

    '''搜索功能封装'''
    def search_goods(self,name):
        self.sendKeys(self.search_input,text=name)
        self.click(self.search_button)

