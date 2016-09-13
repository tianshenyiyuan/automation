# encoding: utf-8
'''
Created on 2016年5月20日

@author: 弈远
'''
import unittest
from common.code import function
from common.code.base import cfg
from testcase.baseCase import BaseCase
# from common.code.base import cfg

class Testcase1(BaseCase):

    def testCase1(self):
#         function.loginSingle()
#         function.navClickTop("采购", "采购订单")
#         function.switchToFrame("main")
#         function.switchToFrame("iframe1", False)
#         function.clickByCssSelector("form#newform_1 input[value='添加']")
#         function.noteDisappear()
#         function.clickById("q_supButt")


        function.loginSingle()
        function.navClickTop("商品", "商品信息")
                   
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()