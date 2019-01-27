#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml
from public.models.log import Log

testData = getyaml(setting.TEST_Element_YAML + '/' + 'setup.yaml')
log = Log()

class setup(Page):
    """
    首页---设置页面
    """
    url = '/'

    # 定位器，通过元素属性定位元素对象
    # 鼠标悬停控件
    userProNick_loc = (By.ID, testData.get_elementinfo(0))
    # 菜单设置元素
    textsetup_loc = (By.XPATH, testData.get_elementinfo(1))
    # 清空昵称文本框
    nick_null_loc = (By.ID,testData.get_elementinfo(2))
    # 昵称文本框元素
    nick_loc = (By.ID, testData.get_elementinfo(3))
    # 清空签名语言本框
    usersign_null_loc = (By.ID, testData.get_elementinfo(4))
    # 签名语言本框元素
    usersign_loc = (By.ID,testData.get_elementinfo(5))
    # 保存元素
    person_info_save_btn_loc = (By.ID,testData.get_elementinfo(6))
    # 鼠标悬停控件
    userProNick1_loc = (By.ID, testData.get_elementinfo(7))
    # 我的新热榜元素
    i_text_loc = (By.XPATH,testData.get_elementinfo(8))

    def dig_setup(self,*data):
        """
        设置操作
        :param data:
        :return:
        """
        # 选择菜单-> 设置
        above = self.find_element(*self.userProNick_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(3)
        self.find_element(*self.textsetup_loc).click()
        sleep(1)
        # 清空昵称文本框并录入数据
        self.find_element(*self.nick_null_loc).clear()
        self.find_element(*self.nick_loc).send_keys(data[0])
        sleep(1)
        # 清空签名文本框并录入数据
        self.find_element(*self.usersign_null_loc).clear()
        self.find_element(*self.usersign_loc).send_keys(data[1])
        sleep(1)
        # 单击保存
        self.find_element(*self.person_info_save_btn_loc).click()
        sleep(1)

    def dig_check_setup(self):
        # 选择菜单-> 我的新热榜
        above = self.find_element(*self.userProNick1_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(3)
        self.find_element(*self.i_text_loc).click()
        sleep(1)
        self.driver.refresh()
        sleep(1)

    nick_error_loc = (By.XPATH,testData.get_CheckElementinfo(0))
    nick_setup_success_loc = (By.XPATH,testData.get_CheckElementinfo(1))
    sign_setup_success_loc = (By.XPATH,testData.get_CheckElementinfo(2))

    def nick_error_hint(self):
        return self.find_element(*self.nick_error_loc).text

    def nick_setup_success_hint(self):
        return self.find_element(*self.nick_setup_success_loc).text

    def sign_setup_success_hint(self):
        return self.find_element(*self.sign_setup_success_loc).text





