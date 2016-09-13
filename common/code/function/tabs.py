# encoding=utf-8
'''
Created on 2016年5月13日

@author: 弈远
'''
from common.code.function import frame
from common.code.base import cfg
def clickBg(driver, name):
    frame.switchTo(driver,"bg_main")
    tabObject = driver.find_element_by_xpath(cfg.getBaseCfg("xpath", "bg_tabs") + "[contains(.,'" + name + "')]") #text()对于含有子节点的情况无效  
    tabObject.click()  


# from selenium import webdriver
# from common.code.function import nav, setValue
# from common.code.function import login
# driver = webdriver.Firefox()
# print login.loginBg(driver)
# nav.clickBg(driver, "网络专区", "商品管理", "录入新品") 
# frame.switchTo(driver,"bg_main")
# setValue.byId(driver, "fconfigid", "test")
#   
