# encoding: utf-8
'''
Created on 2016年5月11日

@author: 弈远
'''
from common.code.base import cfg, log
# from common.code.function import frame
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
class Navigation(object):
    '''
    classdocs
    '''


    def __init__(self, driver):
        self.driver = driver
        '''
        Constructor
        '''
    def clickTop(self, *names):
        '''导航目前分为三级,第一级悬浮菜单项,第二级分组名称可以省略,第三级为导航节点
        
        :Args:
            - names 导航信息
        '''
        if len(names) < 2 or len(names) > 3:
            log.logError("顶部航导航操作错误,名称长度只能为2或者3!")
            return False
        else:
            #首先展开第一级
            navObject = self._getElementByText(self.driver, "navTopMain",names[0])
            #鼠标移入
            ActionChains(self.driver).move_to_element(navObject).perform()
            navObject = self._getElementByText(navObject, "navTopItem",names[1] if len(names) == 2 else names[2])
            try:
                navObject.click()
            except TimeoutException:
                log.logWarn("页面同步超时!") #大页面(例如录入新品)会同步超时,此时页面已经可用,为了不影响流程暂时打印一个警告         
            
    def _getElementByText(self, driverOrElement, cfgName, text):
        return driverOrElement.find_element_by_xpath(cfg.getBaseCfg("xpath", cfgName) + "[contains(text(),'" + text + "')]") 