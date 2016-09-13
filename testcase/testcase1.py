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
        function.loginSingle()
        function.navClickTop("商品", "商品信息")
        function.switchToFrame("main")
        for _ in range(1):
            
            function.clickBtnByText("新增")
            idValueDic = cfg.getIdValueDic("商品信息")
            function.setValues(*idValueDic)
            self._setValueBox(idValueDic[0][u"审核人"], "审核人员", "auForm1")
            function.overlayDisappear()
            self._setValueBox(idValueDic[0][u"复审人"], "复审人员","auForm2")
            function.overlayDisappear()
            function.clickByCssSelector("div.bottomToolbar input[value='保存']")
            function.noteSuccess("添加成功！")
       
    def _setValueBox(self, eleId, section, formName):
        function.clickById(eleId)
        function.setValuesBySection(section)
        function.clickByCssSelector("form#" + formName + " input[value='确定']")
        
                      
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()