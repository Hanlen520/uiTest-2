#coding=utf-8
import pytest
from pages.groupbuy import indexPage
from allure import MASTER_HELPER

'''定义测试类'''
@MASTER_HELPER.feature("主页面测试用例集")
class TestIndex():


    '''测试用例：搜索，需将fixture传入'''
    @MASTER_HELPER.testcase("用例名：搜索东富1号")
    @MASTER_HELPER.step("搜索东富1号")
    def test_search(self,login):
        self.page = indexPage.IndexPage(login)
        self.page.search_goods("东富1号")


    @MASTER_HELPER.step("用例结束后，关闭浏览器")
    def teardown(self):
        self.page.quit()

if __name__ == '__main__':
    pytest.main(['-s','test_index.py'])

