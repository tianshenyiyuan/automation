# encoding=utf-8
'''
Created on 2016年5月11日

@author: 弈远
'''
from common.code.function import wait
from common.code.base import log
from selenium.webdriver.common.action_chains import ActionChains
class Click(object): 
    def __init__(self, driver):
        self.driver = driver
        '''
        Constructor
        '''   
    def clickByCssSelector(self, selector):
        clickObject = self.driver.find_element_by_css_selector(selector)
        clickObject.click()
        
    def clickById(self, htmlId):
        clickObject = self.driver.find_element_by_id(htmlId)
        clickObject.click()
    def acceptIfAlertExists(self, shortTime = False, waitFlag = True):
        self._acceptAlert(shortTime, False, waitFlag)
    def acceptAlert(self, shortTime = False, waitFlag = True):
        self._acceptAlert(shortTime, True, waitFlag)
     
    def clickBtnByText(self, text):
        clickObject = self.driver.find_element_by_xpath("//input[(@type='submit' or @type='reset' or @type='button') and @value='%s'] | //button[text()='%s']" % (text, text))        
        #鼠标移入
        ActionChains(self.driver).move_to_element(clickObject).perform()
        clickObject.click()  
        
    def _acceptAlert(self, shortTime = False, errorFlag = True, waitFlag = True):
        '''
        '添加新商品
        :Args:
            - shortTime 是否短时间
            - errorFlag 不存在时是否记录错误日志
            - waitFlag 是否等待消失

        '''
        alertElement = wait.isAlertPresent(self.driver, shortTime)
        if alertElement:
            alertElement.accept()
            if waitFlag:
                wait.isAlertDisappear(self.driver, shortTime, alertElement) #点击后等待弹出框消失
        else:
            if errorFlag:
                log.logError("弹出框不存在!")
    
def clickByCssSelector(driver, selector):
    Click(driver).clickByCssSelector(selector)
def clickById(driver, htmlId):
    Click(driver).clickById(htmlId)
def clickBtnByText(driver, text):
    Click(driver).clickBtnByText(text)
def acceptAlert(driver):
    Click(driver).acceptAlert()
    