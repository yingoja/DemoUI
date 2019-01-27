#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

from  .driver import browser
import unittest


class MyTest(unittest.TestCase):
    """
    自定义MyTest类
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()