# encoding: utf-8
'''
Created on 2016年5月23日

@author: 弈远
'''
from common.code.base import data

class Value(object):
    '''
    classdocs
    '''


    def __init__(self, driver):
        self.driver = driver
    def saveById(self, htmlid, key):
        '''保存页面值到数据字典
        Args:
            -htmlid: 控件id
            -key: 数据键值
        '''
        ele = self.driver.find_element_by_id(htmlid)
        data.setData(key, ele.get_attribute("value"))