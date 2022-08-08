#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

# from  .driver import browser
from selenium import webdriver
import unittest



class MyTest(unittest.TestCase):
    """
    自定义MyTest类
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://dig.chouti.com/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()