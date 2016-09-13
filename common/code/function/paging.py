# encoding=utf-8
'''
Created on 2016年5月13日

@author: 弈远
'''
from common.code.base import cfg, log
from common.code.function import element
class Paging(object):
    '''
    classdocs
    '''
    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver

    def next(self):
        '''                 
        '''
        return self._pag("bg_paging_next")
    def prev(self):
        '''                 
        '''
        return self._pag("bg_paging_prev")
    def first(self):
        '''                 
        '''
        return self._pag("bg_paging_first")
    def last(self):
        '''                 
        '''
        return self._pag("bg_paging_last") 
    def num(self, number):
        #在指定页的时候直接返回
        if int(number) == int(self.currNum()):
            log.logDone("当前已经是第%d页,未进行翻页." % number)
            return True
        try:
            numberObject= element.byText(self.driver, number, cfg.getBaseCfg("xpath", "bg_paging"))
            numberObject.click()
            #同步分页栏加载完毕
            self._wait() 
        except:
            return False  
    def currNum(self):  
        numberObject= self.driver.find_element_by_xpath(cfg.getBaseCfg("xpath", "bg_curPagNum"))
        return numberObject.text
    def _pag(self, name):
        """
        name: bg_paging_prev(上一页),bg_paging_next(下一页),bg_paging_first(首页),bg_paging_last(末页)
        """
        try:
            nextObject= element.byText(self.driver, cfg.getBaseCfg("text", name), cfg.getBaseCfg("xpath", "bg_paging"))
            nextObject.click()
            #同步分页栏加载完毕
            self._wait()
            return True
        except:
            #在首页的时候点击上一页或首页或在尾页的时候点击下一页或尾页直接返回False
            return False
    def _wait(self):
        self.driver.find_element_by_id( cfg.getBaseCfg("id", "bg_paging"))
  
# from selenium import webdriver
# driver = webdriver.Chrome()
# print login.loginBg(driver)
# nav.clickBg(driver, "票务前台", "订单处理", "客人取票")
# frame.switchTo(driver,"bg_main")
# # clickBg(driver, "检索结果")
# tabs.clickBg(driver, "已支付 审核至前台")
# 
# test = Paging(driver)
# print  test.currNum()
# test.next()
# print  test.currNum()
# test.prev()
# print  test.currNum()
# test.last()
# print  test.currNum()
# test.first()
# print  test.currNum()
# test.num(2)
# print  test.currNum()
# test.num(2)
# print  test.currNum()
# test.num(8)
# print  test.currNum()


