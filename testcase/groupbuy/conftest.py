#coding=utf-8
import pytest
from pages.groupbuy import loginPage
from selenium import webdriver
from allure import MASTER_HELPER
import time

'''登录函数，供全局使用'''
@pytest.fixture(scope="module")
def login():
    driver=webdriver.Chrome()
    driver.maximize_window()
    page=loginPage.LoginPage(driver)
    page.login("17826826147","zyk123456")
    return driver




