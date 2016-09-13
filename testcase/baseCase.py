# encoding=utf-8
'''
Created on 2016年9月12日

@author: kun.wang
'''
import unittest
from selenium import webdriver
from common.code import function

class BaseCase(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        function.driver = self.driver


    def tearDown(self):
        pass


    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()