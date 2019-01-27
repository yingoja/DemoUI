#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import yaml

class getyaml:
    def __init__(self,filepath):
        self.path = filepath

    def get_yaml(self):
        '''
        加载yaml文件数据
        :param path: 文件路径
        :return:返回数据
        '''
        try:
            f = open(self.path,encoding='utf-8')
            data =yaml.load(f)
            f.close()
            return data
        except Exception as msg:
            print("异常消息-> {0}".format(msg))

    def alldata(self):
        """
        读取yaml文件数据
        :return: 返回数据
        """
        data =self.get_yaml()
        return data

    def caselen(self):
        """
        testcase字典长度
        :return: 字典长度大小
        """
        data = self.alldata()
        length = len(data['testcase'])
        return length

    def checklen(self):
        """
        check字典长度
        :return: 字典长度大小
        """
        data = self.alldata()
        length = len(data['check'])
        return length

    def get_elementinfo(self,i):
        """
        获取testcase项的element_info元素
        :param i: 位置序列号
        :return: 返回element_info元素数据
        """
        data = self.alldata()
        return data['testcase'][i]['element_info']

    def get_find_type(self,i):
        """
        获取testcase项的find_type元素数据
        :param i: 位置序列号
        :return: 返回find_type元素数据
        """
        data = self.alldata()
        return data['testcase'][i]['find_type']

    def get_operate_type(self,i):
        """
        获取testcase项的operate_type元素数据
        :param i: 位置序列号
        :return: 返回operate_type元素数据
        """
        data = self.alldata()
        return data['testcase'][i]['operate_type']

    def get_CheckElementinfo(self,i):
        """
        获取check项的element_info元素
        :param i: 位置序列号
        :return: 返回element_info元素数据
        """
        data = self.alldata()
        return data['check'][i]['element_info']

    def get_CheckFindType(self,i):
        """
        获取check项的element_info元素
        :param i: 位置序列号
        :return: 返回find_type元素数据
        """
        data = self.alldata()
        return data['check'][i]['find_type']

    def get_CheckOperate_type(self,i):
        data = self.alldata()
        return data['check'][i]['operate_type']

