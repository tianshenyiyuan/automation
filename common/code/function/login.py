# encoding: utf-8
'''
Created on 2016年5月10日

@author: 弈远
'''
from common.code.base import cfg, log
from common.code.function import setValue, click

class Login(object):
    '''
    classdocs
    '''
    def __init__(self, driver):
        self.driver = driver
        self.flag = False  # 登录成功标识
        self.driver.implicitly_wait(cfg.getBaseCfg("time", "waitTime"))
        self.driver.set_page_load_timeout(cfg.getBaseCfg("time", "loadingTime"))
        self.driver.maximize_window()
        '''
        Constructor
        '''
    def login(self, url, user, pwd):
        self.driver.get(url)
        setValue.byIds(self.driver, {cfg.getBaseCfg("id", "userName"):user, cfg.getBaseCfg("id", "pwd"):pwd})
        #setValue.setCity(self.driver, cfg.getBaseCfg("id", "citySelect"), cfg.getBaseCfg("id", "city"), city)
        click.clickById(self.driver, cfg.getBaseCfg("id", "loginBtn"))
        # 验证是否登录成功
        try:
            # 找到登录成功标识则登录成功
            self._getExitObject()        
            self.flag = True
            #刷新一下解决新版提示问题
            self.driver.refresh()
            return True 
        except Exception, e:
            log.logError("登录错误,退出链接没有找到!")
            log.logError(e.msg)
        
    def logout(self):
        exitObject = self._getExitObject()
        exitObject.click()
        click.acceptAlert(self.driver)
        return True
    
    def _getExitObject(self):
        return self.driver.find_element_by_link_text(cfg.getBaseCfg("text", "loginFlag"))

