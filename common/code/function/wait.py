# encoding=utf-8
'''
Created on 2016年5月18日

@author: 弈远
'''
from common.code.base import cfg, log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from distutils.log import Log

class Wait(object):
    '''
    classdocs
    '''
    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver
        self.waitTime = int(cfg.getBaseCfg("time", "waitTime"))
        self.wait = WebDriverWait(driver, self.waitTime)
        self.shortTime = int(cfg.getBaseCfg("time", "shortTime"))
        self.shortWait = WebDriverWait(driver, self.shortTime)

    def waitObjDisappear(self, classKey): #同步对象消失
        #响应时间设置为1秒,等待对象弹出
        try:         
            self.driver.implicitly_wait(0) #隐式时间设置为0
            WebDriverWait(self.driver, 1).until(lambda x : x.find_element_by_class_name(cfg.getBaseCfg("class", classKey)).is_displayed())
        except TimeoutException:
            return True
        except StaleElementReferenceException:
            return True
        finally:
            self.driver.implicitly_wait(cfg.getBaseCfg("time", "waitTime"))
        def disappear(driver):
            try:
                self.driver.implicitly_wait(0) #隐式时间设置为0
                element = driver.find_element_by_class_name(cfg.getBaseCfg("class", classKey))
                return not element.is_displayed()
            except NoSuchElementException:
                return True
            except StaleElementReferenceException:
                return True
            finally:
                self.driver.implicitly_wait(cfg.getBaseCfg("time", "waitTime"))      
        return self.wait.until(disappear)
        
#     def noteSuccess(self, content = None):
#         """
#         note_success 成功提示消息是否准确
#         :Args:
#             -content 预期提示内容
#         """
#         try:
#             infoObject = self.driver.find_element_by_class_name(cfg.getBaseCfg("class", "note_success"))
#             #同步成功框显示
#             try:
#                 self.wait.until(lambda x : infoObject.is_displayed())
#                 innerText = unicode(infoObject.get_attribute("innerText"))
#                 if innerText.strip() == unicode(content.strip()) :
#                     
#                     return True
#                 else:
#                     log.logError("成功通知框不符合预期!预期为:%s,实际为:%s" % (content, innerText))
#                     return False
#             except TimeoutException:
#                 log.logError("成功通知框不消不可见!")
#                 return False
#             except StaleElementReferenceException:
#                 log.logError("成功通知框不已经消失!")
#                 return False
#         except NoSuchElementException:
#             log.logError("成功通知框不没有弹出!")
#             return False
    def note(self, content = None, noteType = "info"):
        """
        note信息通知方法
        :Args:
            -content 预期提示内容
            -noteType 消息类型 info,warn,success or error
        """
        if noteType == "info":
            key = "note_info"
            name = "消息"
        elif noteType == "success":
            key = "note_success"
            name = "成功"
        elif noteType == "warn":
            key = "note_warn"
            name = "警告"
        elif noteType == "error":
            key = "note_error"
            name = "失败"
        else:
            log.logError("通知框类型选择错误!")
            return False
        try:
            infoObject = self.driver.find_element_by_class_name(cfg.getBaseCfg("class", key))
            #同步成功框显示
            try:
                self.wait.until(lambda x : infoObject.is_displayed())
                innerText = unicode(infoObject.get_attribute("innerText"))
                if innerText.strip() == unicode(content.strip()) :
                    
                    return True
                else:
                    log.logError(name + "通知框不符合预期!预期为:%s,实际为:%s" % (content, innerText))
                    return False
            except TimeoutException:
                log.logError(name + "通知框不消不可见!")
                return False
            except StaleElementReferenceException:
                log.logError(name + "通知框不已经消失!")
                return False
        except NoSuchElementException:
            log.logError(name + "通知框不没有弹出!")
            return False    
        
    def ready(self):
        pass
    def disappear(self):
        pass
    def titleIs(self, title):
        """
        Title是否为指定值
        """
        return EC.title_is(unicode(title))(self.driver)
    
    def titleContains(self, title):
        """
        Title是否包含预期字符去
        """
        return EC.title_contains(unicode(title))(self.driver)   
    def isAlertPresent(self, shortTime = False):
        """
        '等待弹出框出现
        :Args:
            -shortTime true表示短时间,false表示长时间
        """
        try:
            return  self._getWait(shortTime).until(lambda x : EC.alert_is_present()(x))
        except TimeoutException:
            return False
    def isAlertDisappear(self, shortTime = False, alertElement = None):
        """
        '等待弹出库是否消失
        :Args:
            -shortTime true表示短时间,false表示长时间
        """
        try:
            return  self._getWait(shortTime).until(lambda x : not EC.alert_is_present()(x))
        except TimeoutException:
            return False
    def windowCount(self, num):
        try:
            return self.wait.until(lambda x : len(x.window_handles) == (num + 1))
        except TimeoutException:
            return False
    def _getWait(self, shortTime = False):
        if shortTime :
            return self.shortWait
        else:
            return self.wait
    
def isAlertPresent(driver, shortTime = False):
    return Wait(driver).isAlertPresent(shortTime)
def isAlertDisappear(driver, shortTime = False, alertElement = None):
    return Wait(driver).isAlertDisappear(shortTime ,alertElement)
def windowCount(driver, num):
    return Wait(driver).windowCount(num)
#     def test_presence_of_element_located(self):
#       ''' 判断element是否出现在dom树 '''
#       locator = (By.ID, search_text_field_id)
#       search_text_field_should_present = EC.visibility_of_element_located(locator)
#       self.assertTrue(search_text_field_should_present(dr))
#     
#     def test_visibility_of(self):
#       search_text_field = dr.find_element_by_id(search_text_field_id)
#       search_text_field_should_visible = EC.visibility_of(search_text_field)
#       self.assertTrue(search_text_field_should_visible('yes'))
#     
#     def test_text_to_be_present_in_element(self):
#       text_should_present = EC.text_to_be_present_in_element((By.NAME, 'tj_trhao123'), 'hao123')
#       self.assertTrue(text_should_present(dr))


# 　 elm = wait.until(lambda x: x.find_element_by_xpath(Xpath))
