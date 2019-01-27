#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Administrator'


import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
CONFIG_DIR = os.path.join(BASE_DIR,"database","user.ini")
# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR,"testcase")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR,"logs")
# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR,"testdata")
# 元素控件
TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml")
