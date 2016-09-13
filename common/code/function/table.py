# encoding: utf-8
'''
Created on 2016年5月11日

@author: 弈远
'''
from common.code.base import cfg, log
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
class Table(object):
    '''
    classdocs
    '''
    def __init__(self, driver, tableId=cfg.getBaseCfg("id", "bg_table")):
        '''
        Constructor
        '''
        self.driver = driver
        self.tableId = tableId
        self.dic = dict() #表头与表格对象键值对
        tableObject = driver.find_element_by_id(tableId)
        trObjects = tableObject.find_elements_by_css_selector("table>tbody>tr")
        self.count = len(trObjects)
        if len(trObjects) < 1:
            log.logError("表格操作错误,表格为空!")
        else:
            #处理表头(th)
            valuesTh = []
            thobjs = trObjects[0].find_elements_by_tag_name("th")
            try:
                self.checkAllObect = thobjs[0].find_element_by_tag_name("input")                      
            except NoSuchElementException:
                #不存在复选框时自动跳过
                pass
            for obj in thobjs:
                valuesTh.append(obj.text if obj.text != "" else "checkBox") #没有text的为复选框
            #将td内容存储的dic.以表头为键值
            for i in range(1,len(trObjects)):
                tdobjs = trObjects[i].find_elements_by_tag_name("td")
                for j in range(len(tdobjs)):
                    if self.dic.get(valuesTh[j]) == None:
                        self.dic[valuesTh[j]] = []
                    self.dic[valuesTh[j]].append(tdobjs[j])                  
    def checkAll(self):
        if not self.checkAllObect.is_selected():
            self.checkAllObect.click()
    def uncheckAll(self):
        if self.checkAllObect.is_selected()():
            self.checkAllObect.click()
    def checkByNum(self, numbers):
        '''
        '''
        self._chenkNum(True, numbers)
    def uncheckByNum(self, numbers):
        '''
        '''
        self._chenkNum(False, numbers)
    
    def chekByContent(self, name, value):
        self._chekContent(True, name, value)
    def unchekByContent(self, name, value):
        self._chekContent(False, name, value)
    def clickByContent(self, name, value, clickName = "", clickColName=cfg.getBaseCfg("text", "bg_clickColName")):
        '''
            clickColName:需要点击的列名称默认为操作
            clickName: 需要点击的名称
        '''        
        
        if clickName == "":
            clickName = value[0] if type(value) in [list, set, tuple] else value #默认取值的第一项
            clickName = unicode(clickName)
            clickColName  = name[0] if type(name) in [list, set, tuple] else name #默认取名称的第一项
            clickColName = unicode(clickColName)
        if unicode(clickColName) in self.dic:
            dic = self._getDic(name, value)
            count = self._getNumByContent(dic)
            if count > -1 :
                clickObject = self.dic[clickColName][count].find_element_by_xpath("a[contains(text(),'" + str(clickName) + "')]")
                clickObject.click()
            else:
                log.logError("未找到指定记录!")
        else:
            raise Exception("操作列%s不存在!" % clickColName)
            log.logError("操作列%s不存在!" % clickColName)

    
    def _chekContent(self, flag, names, values):
        dic = self._getDic(names, values)
        count = self._getNumByContent(dic)
        if count != -1 :
            self._chenkNum(flag, count + 1)
        else:
            log.logError("未找到指定记录!")
    def _chenkNum(self, flag, numbers):
        checkObxObjects = self.dic.get("checkBox")
        if type(numbers) == int:
            numbers = [numbers]
        for num in numbers:
            if num > len(checkObxObjects) or num < 1:
                log.logError("数字%d超出复选框总数范围,未选择." %num)
            else:  
                #使用actions先将移动到点击元素,解决报错问题
                actions = ActionChains(self.driver)
                actions.move_to_element(checkObxObjects[num - 1])
                actions.perform()
                checkObxObject = checkObxObjects[num - 1].find_element_by_tag_name("input")
                if checkObxObject.is_selected() != flag:
                    checkObxObject.click()
    def _getDic(self, names, values):
        dic = {}
        if isinstance(names,basestring) and isinstance(values,basestring):
            dic[unicode(names)] = unicode(values)
        elif type(names) in [list, set, tuple] and type(values) in [list, set, tuple]:
            if len(names) > len(values):
                raise Exception("名称列表大于值列表!")
            else:
                for i in range(len(names)):
                    dic[unicode(names[i])] = unicode(values[i])  
        else:
            raise Exception("参数传递错误,name和value必须同时为字符串或者同时为列表!")
        return dic    
    def _getNumByContent(self, nvDic):
        '''
        nvDic: 需要匹配的键值对
        '''
        num = -1
        tempDic = dict() #存放临时数据用于比较
        for name in nvDic:
            if not unicode(name) in self.dic:
                log.logError("列%s不存在." % name)
                raise NameError('%s名称错误!' % name)
            else:
                nvDic[name] = nvDic[name].strip() #去除空格
        
        for i in range(self.count -1):
            tempDic.clear()
            for name in nvDic:
                tdObject = self.dic[unicode(name)][i] 
                tempDic[name] = tdObject.text.strip()
            if tempDic == nvDic:
                num = i
                break
        return num        
#
# from selenium import webdriver
# driver = webdriver.Chrome()
# print 100
# from common.code.function import login,nav,frame
# print login.loginBg(driver)


# nav.clickBg(driver, "票务前台", "订单处理", "客人取票")
# frame.switchTo(driver,"bg_main")
# a = Table(driver)
# a.checkByNum([0,6,7,8,9,10,11,100])
# a.uncheckByNum(0,6,7,8,9,10,11,100)
# a.uncheckByNum(0,6,7,8,9,10,11,100)
# a.clickByContent(["订单号","支付方式"], ["12037193","支付宝"])
class SimpleTable(object):
    '''
    classdocs
    '''
    def __init__(self, driver, tableId):
        '''
        Constructor
        '''
        self.driver = driver
        self.tableId = tableId
        self.dic = dict() #表头与表格对象键值对
        self.tableObject = driver.find_element_by_id(tableId)
                        
    def selectAllCheckbox(self):
        for ele in self.tableObject.find_elements_by_css_selector("input[type='checkbox']"):
            if not ele.is_selected():
                ele.click()


