# encoding=utf-8
'''
Created on 2016年5月11日

@author: 弈远
'''
from selenium.webdriver.support.ui import Select
from common.code.base import log, cfg
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from common.code.function import element as ele
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from common import picDir

class Value(object):
    '''
    classdocs
    '''


    def __init__(self, driver):
        self.driver = driver
        self.shortTime = int(cfg.getBaseCfg("time", "shortTime"))
        self.wait = WebDriverWait(driver, self.shortTime)
        '''
        Constructor
        '''
    def setValuesByClass(self, classDic, valueDic):
        '''批量赋值(class name)
        
        :Args:
            - idOrNameDic id或name组成的字典
            - valueDic值字典
        '''
        for key in classDic:
            if key in valueDic: #数据字典中存在时进行赋值
                inputEle = self.driver.find_element_by_class_name(classDic[key])
                self._by(inputEle, classDic[key], valueDic[key])                
            else:
                log.logWarn("%s字段值在数据字典中不存在,跳过赋值!" % key)
    def setValues(self, idOrNameDic, valueDic):
        '''批量赋值
        
        :Args:
            - idOrNameDic id或name组成的字典
            - valueDic值字典
        '''
        for key in idOrNameDic:
            if key in valueDic and valueDic[key].strip() != "" : #数据字典中存在时进行赋值
                ""
#                 inputEle = self.driver.find_element_by_css_selector("*[name='%s'],[id='%s']" % (idOrNameDic[key],idOrNameDic[key]))
#                 htmlid = inputEle.get_attribute("id")
#                 if htmlid != None and htmlid == idOrNameDic[key]:
#                     self._by(inputEle, idOrNameDic[key], valueDic[key])
#                 else:
#                     self.byName(idOrNameDic[key], valueDic[key])
                #wk -- 2016-09-09 目前系统中的控件都有id,全部使用id赋值
                inputEle = self.driver.find_element_by_id(idOrNameDic[key])
                self._by(inputEle, idOrNameDic[key], valueDic[key])
            else:
                log.logWarn("%s字段值在数据字典中不存在或者值为空,跳过赋值!" % key)
                
    def byIds(self, idValue):
        for key in idValue:
            self.byId(key, idValue[key])
    def byName(self, name, value = "", elements = None):       
        elements = self.driver.find_elements_by_name(name) if elements == None else elements
        if len(elements) == 0:
            log.logError("%s控件不存在." % name)
            return
        else:
            inputType =  elements[0].get_attribute("type")
            if inputType == 'checkbox' or inputType == 'radio':  #单选复选按钮按后面的值进行选择
                if value == None or value.strip() == "": #值为空时默认选择第一个
                    self._select( elements[0])
                else:
                    #checkbox支持多选
                    if inputType == 'checkbox':
#                         if type(value) in [tuple, list, set]:
#                             flag = True
#                         elif ";" in value:
#                             value = value.split(";")
#                             flag = True
#                     if flag: 
                        if type(value) in [tuple, list, set]:
                            pass
                        elif ";" in value:
                            value = value.split(";")
                        else:
                            value = [value]
                        tempList = map(lambda x : unicode(x).strip(), value)
                        for element in elements:     
                            text = self._getNextText(element).strip()
                            if text in tempList:
                                self._select(element)
                                tempList.remove(text) #选中的进行移除
                            else:
                                self._unselect(element)
                        for val in tempList:
                            log.logError("%s控件文本值'%s'未找到." %(name, val))
                    else:        
                        for element in elements:     
                            text = self._getNextText(element)
                            if unicode(value.strip()) == unicode(text.strip()):
                                self._select(element)
                                break
                        else:
                            log.logError("%s控件文本值'%s'未找到." %(name, value))
                            
                            
            else: #按基础逻辑处理
                for element in elements:
                    if element.is_displayed():
                        self._by(element, name, value)
                    else:
                        log.logWarn("控件不可见,自动忽略!")
                    
    def byId(self, htmlId, value, element = None):
        
        element = self.driver.find_element_by_id(htmlId) if element == None else element
        self._by(element, htmlId, value)

    def selectByText(self, htmlId, text, element = None):
        selectObject = Select(self.driver.find_element_by_css_selector("*[name='%s'],[id='%s']" % (htmlId, htmlId)) if element == None else element)
        if text == None or text.strip()=='': # 为空时默认选择第一个
            selectObject.select_by_index(1)
        else:
            selectObject.select_by_visible_text(text)
    def setCheckboxCascaded(self, htmlName, valueDic): 
        '''
        '级联样式的Checkbox设置
        '''
        elements = self.driver.find_elements_by_name(htmlName)
        #value作为键值装入dic
        eleDic = {}
        for element in elements:
            eleDic[self._getNextText(element).strip()] = element
            
        for key in valueDic:
            if eleDic.has_key(unicode(key)):
                parentEle = eleDic[unicode(key)]
                self._select(parentEle)
                subValue = valueDic[key]
                if type(subValue) in [tuple, list, set]:  
                    subValue = map(lambda x : unicode(x).strip(), subValue)
                elif subValue == None or "" == subValue.strip():
                    subValue = [key] #为空时子复选框与父复选框名称相同
                elif type(subValue) == str or type(subValue) == unicode:
                    subValue = [unicode(subValue)] 
                else:
                    log.logError("%s的子复选框值类型不支持,类型为:%s."  % (key, type(subValue)))
                    continue
                subEles = ele.firstChild(ele.nextSibling(ele.parent(parentEle))).find_elements_by_tag_name("input")
                for subEle in subEles:
                    subText = self._getNextText(subEle).strip()
                    if subText in subValue:
                        self._select(subEle)
                        subValue.remove(subText)
                    #全部匹配到后直接退出
                    if len(subValue) == 0: 
                        break
                for value in subValue:
                    log.logError("%s的子复选框值不存在,值为:%s."  % (key, value))        
            else:
                log.logError("%s的父复选框不存在."  % key)
    def setValueList(self, htmlName, valueList, begin = 0):
        '''
        '级联样式的Checkbox设置
        '''
        elements = self.driver.find_elements_by_name(htmlName)
        i = 0
        j = 0
        valueLen = len(valueList)
        for ele in elements:
            if i <= begin:
                i = i + 1
                continue
            if valueLen <= j: #value长度小于等于对象个数时直接退出循环
                break
            self._by(ele, htmlName, valueList[j])
            j = j + 1
    def setCity(self, citySelectId, hiddenId, value):
        '''
        '设置city
        ''' 
        #获取id值
        cityEle = self.driver.find_element_by_id(citySelectId)
        cityEle.click()
        cityEle = self.driver.find_element_by_class_name(cfg.getBaseCfg("class", "bg_citybox"))
        cityEle = cityEle.find_element_by_link_text(value)
        cityId = cityEle.get_attribute(cfg.getBaseCfg("attr", "bg_cityid"))
        hiddenEle = self.driver.find_element_by_id(hiddenId) 
        self.driver.execute_script("arguments[0].value = '" + cityId + "'" , hiddenEle )
        #hiddenEle.send_keys(cityId)                           
    def _sendKeys(self, element, value):
        element.clear()
        element.send_keys(unicode(value))  
    def _getNextText(self, element):
        '''
        '获取当前元素后面的文本值
        '''
        return unicode(self.driver.execute_script("return arguments[0].nextSibling.nodeValue", element))
    def _select(self, element):
        if not element.is_selected():
            if not element.is_enabled():
                log.logError("对象不可用,未选中!")
            else:
                element.click()
    def _unselect(self, element):
        if element.is_selected():
            if not element.is_enabled():
                log.logError("对象不可用,未取消选中!")
            else:
                element.click()
    def _by(self, element, attr, value):
        '''
            attr : id或者name值
        '''
        print "--------------------> %s = %s" % (attr, value)
        #等待1秒,解决控件级联的问题
        try:
            self.wait.until(lambda x : element.is_enabled())
        except TimeoutException:
            log.logWarn("%s控件不可用,跳过赋值." % attr)
            return
        tagName = element.tag_name
        if tagName == "select":
            self.selectByText(attr, value, element)
        elif tagName == "input":
            inputType =  element.get_attribute("type")
            if inputType == "password":
                self._sendKeys(element, value)
            elif inputType == "text":
                if "isDateF" in element.get_attribute("class"): #日期控件有自动添加-功能去除日期串中的"-"
                    value = value.replace("-", "")
                self._sendKeys(element, value)
#                 onFocus = element.get_attribute("onFocus")
#                 if onFocus != None and onFocus.startswith("WdatePicker") : #日期控件(WdatePicker)       
#                     if element.get_attribute("readonly") : #只读需要修改为非只读
#                         self.driver.execute_script("arguments[0].removeAttribute('readonly')", element)
#                         self._sendKeys(element, value)
#                         self.driver.execute_script("arguments[0].setAttribute('readonly', true)", element)
#                     else:
#                         self._sendKeys(element, value)
#                     #点击一下form,切掉显示的日期控件
#                     #self.driver.find_element_by_tag_name("form").click()  #点击form容易点击到按钮
#                     #修改为发送右键加esc键
#                     ActionChains(self.driver).context_click(element).perform()
#                     element.send_keys(Keys.ESCAPE)
#                 else:
#                     self._sendKeys(element, value)
                   
            elif inputType == 'checkbox' or inputType == 'radio':
                elements = self.driver.find_elements_by_id(attr)
                if len(elements) == 0:
                    log.logError("%s控件不存在." % attr)
                    return
                else:
                    inputType =  elements[0].get_attribute("type")
                    if value == None or value.strip() == "": #值为空时默认选择第一个
                        self._select( elements[0])
                    else:
                        #checkbox支持多选
                        if inputType == 'checkbox':
                            if type(value) in [tuple, list, set]:
                                pass
                            elif ";" in value:
                                value = value.split(";")
                            else:
                                value = [value]
                            tempList = map(lambda x : unicode(x).strip(), value)
                            for element in elements:     
                                text = self._getNextText(element).strip()
                                if text in tempList:
                                    self._select(element)
                                    tempList.remove(text) #选中的进行移除
                                else:
                                    self._unselect(element)
                            for val in tempList:
                                log.logError("%s控件文本值'%s'未找到." %(attr, val))
                        else:        
                            for element in elements:     
                                text = self._getNextText(element)
                                if unicode(value.strip()) == unicode(text.strip()):
                                    self._select(element)
                                    break
                            else:
                                log.logError("%s控件文本值'%s'未找到." %(attr, value))       
            elif inputType == "file":
                #图片路径分隔符处理
                value = value.replace("/", os.path.sep)
                value = value.replace("\\", os.path.sep)
                #相对路径
                if not os.path.exists(value):
                    value = picDir + value
                element.send_keys(value)         
            else:
                log.logError("文本控件类型%s不支持,标识为:%s" % (inputType, attr))
        elif tagName == "textarea" :
            self._sendKeys(element, value)
        elif tagName == "div": #富文本框处理目前仅支持edui-editor 
            #文本框在下一层,取id
            editorObject = self.driver.execute_script("return arguments[0].firstChild", element)
            if unicode(editorObject.get_attribute("class")).strip() != unicode("edui-editor"):
                log.logError("非输入控件,标识为:%s" % attr)  
            else:
                editorId = editorObject.id
                #获取是第几个富文本示例
                num = -1
                editorObjects = self.driver.find_elements_by_class_name("edui-editor")
                for i in range(len(editorObjects)):
                    if unicode(editorObjects[i].id) == unicode(editorId):
                        num = i
                        break
                if num == -1:
                    log.logError("非输入控件,标识为:%s" % attr) 
                else:
                    self.driver.execute_script("UE.instants.ueditorInstant%d.setContent(arguments[0])" % num, value)
        
        else:
            log.logError("非输入控件,标识为:%s" % attr)      

def byIds(driver, idValue):
    Value(driver).byIds(idValue)
def byId(driver, htmlId, value):
    Value(driver).byId(htmlId, value)
def selectByText(driver, htmlId, text):
    Value(driver).selectByText(htmlId, text)
def byName(driver, name, text):
    Value(driver).byId(name, text)
def setCity(driver, citySelectId, hiddenId, value):
    '''
    '设置city
    ''' 
    Value(driver).setCity(citySelectId, hiddenId, value)