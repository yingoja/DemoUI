#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'


import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting
from public.models import myunit,screenshot
from public.page_obj.setupPage import setup
from public.page_obj.loginPage import login
from public.models.log import Log

f_login = open(setting.TEST_DATA_YAML + '/' + 'login_data.yaml',encoding='utf-8')
LoginData = yaml.load(f_login)
ph = LoginData[5]['data']['phone']
pwd = LoginData[5]['data']['password']

try:
    f_setup =open(setting.TEST_DATA_YAML + '/' + 'setup_data.yaml',encoding='utf-8')
    SetupData = yaml.load(f_setup)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))

@ddt.ddt
class Demo_UI(myunit.MyTest):
    """首页---设置"""
    def user_login_verify(self,phone,password):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :return:
        """
        login(self.driver).user_login(phone,password)

    def exit_login_check(self):
        """
        退出登录
        :return:
        """
        login(self.driver).login_exit()

    def setup_test(self,*args):
        setup(self.driver).dig_setup(*args)

    @ddt.data(*SetupData)
    def test_setup(self,datayaml):
        """
        首页---设置操作测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'],datayaml['detail']))

        # 调用登录方法
        self.user_login_verify(ph,pwd)

        # 调用设置接口
        self.setup_test(datayaml['data']['name'],datayaml['data']['sign'])
        po = setup(self.driver)
        if datayaml['screenshot'] == 'name_empty':
            log.info("检查点-> {0}".format(po.nick_error_hint()))
            self.assertEqual(po.nick_error_hint(),datayaml['check'][0]),"返回实际结果是->: {0}".format(po.nick_error_hint())
            log.info("返回实际结果是->: {0}".format(po.nick_error_hint()))
            screenshot.insert_img(self.driver, datayaml['screenshot'] + '.jpg')
            self.exit_login_check()
        else:
            po.dig_check_setup()
            log.info("检查点-> {0}和{1}".format(po.nick_setup_success_hint(),po.sign_setup_success_hint()))
            self.assertEqual(po.nick_setup_success_hint(), datayaml['check'][0]), "返回实际结果是->: {0}".format(po.nick_setup_success_hint())
            self.assertEqual(po.sign_setup_success_hint(), datayaml['check'][1]), "返回实际结果是->: {0}".format(po.sign_setup_success_hint())
            log.info("返回实际结果是->: {0}和{1}".format(po.nick_setup_success_hint(),po.sign_setup_success_hint()))
            screenshot.insert_img(self.driver, datayaml['screenshot'] + '.jpg')
            self.exit_login_check()

if __name__=='__main__':
    unittest.main()