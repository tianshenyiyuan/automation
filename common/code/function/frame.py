# encoding=utf-8
'''
Created on 2016年5月11日

@author: 弈远
'''
from common.code.base import cfg
def switchTo(driver, name, default = True):
    if default:
        driver.switch_to_default_content()  #进入下层frame后需要跳出处理
    
    try: #异常时,先查元素在匹配
        frameName = cfg.getBaseCfg("frame", name)
        frameName = name if frameName.strip() == "" else frameName
        driver.switch_to.frame(frameName)
    except:
        frameObject = driver.find_element_by_css_selector("frame[name='" + frameName +"'],iframe[name='" + frameName +"']")
        driver.switch_to.frame(frameObject)
