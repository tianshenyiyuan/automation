# encoding=utf-8
'''
Created on 2016年5月17日

@author: 弈远
'''
from common.code.base import cfg
from selenium import webdriver
from .login import Login
from .click import Click
from .element import Element
from .nav import Navigation
from .paging import Paging
from .table import Table,SimpleTable
from .setValue import Value
from .saveValue import Value as SaveValue
from .window import Window
from .wait import Wait
import frame
from common.code.function import tabs
driver = None

#登录相关方法
def loginSingle(name=cfg.getCfg("登录_单体", "用户名"), pwd=cfg.getCfg("登录_单体", "密码")):
    '''单体登录     
    
    :Args:
        - name 用户名
        - pwd 密码
    '''
    return Login(driver).login(cfg.getCfg("url", "单体"), name, pwd)
    
def logoutSingle():
    '''单体退出      

    :Args:
        
    '''
    return Login(driver).logout()


#对象点击
def clickByCssSelector(selector):
    '''通过css选择器点击对象      

    :Args:
        - selector css选择器
    '''
    return Click(driver).clickByCssSelector(selector)
def clickById(htmlId):
    '''通过id点击对象      

    :Args:
        - htmlId 对象id
    '''
    return Click(driver).clickById(htmlId)
def acceptIfAlertExists(shortTime = False, waitFlag = True):
    '''如果弹出框存在点击弹出框确认按钮否则不做任何操作

    :Args:
        - shortTime 是否短等待,默认为长等待
        - waitFlag 是否等待,默认等待
    '''
    return Click(driver).acceptIfAlertExists(shortTime, waitFlag)
def acceptAlert(shortTime = False, waitFlag = True):
    '''点击弹出框确认按钮

    :Args:
        - shortTime 是否短等待,默认为长等待
        - waitFlag 是否等待,默认等待
    '''
    return Click(driver).acceptAlert(shortTime, waitFlag)
def clickBtnByText(text):
    '''通过文本内容点击按钮

    :Args:
        - text 文本值
    '''    
    Click(driver).clickBtnByText(text)
    
#对象获取
def getByText(text, basePath=""):
    '''通过文本内容获取对啊ing

    :Args:
        - basePath 基础路径,为空时使用绝对路径
    
    '''
    return Element(driver).byText(text, basePath="")
    
def nextSibling(element):
    '''获取后置对象

    :Args:
        - element 当前对象
    
    '''
    return Element(driver).nextSibling(element)
def parent(element):
    '''获取父对象

    :Args:
        - element 当前对象
    
    '''
    return Element(driver).parent(element)
def previousSibling(element):
    '''获取前置对象

    :Args:
        - element 当前对象
    
    '''
    return Element(driver).previousSibling(element)
def firstChild(element):
    '''获取第一个子对象

    :Args:
        - element 当前对象
    
    '''
    return Element(driver).firstChild(element)
def lastChild(element):
    '''获取最后一个子对象

    :Args:
        - element 当前对象
    
    '''
    return Element(driver).lastChild(element)
def allChild(element):
    '''获取全部子对象组成的列表

    :Args:
        - element 当前对象
    
    '''
    return Element(driver).allChild(element)
def child(element, index):
    '''通过序号获取子对象

    :Args:
        - element 当前对象
        - index 序号
    
    '''
    return Element(driver).child(element, index)
    
#Frame
def switchToFrame(name, default = True):
    '''frame跳转

    :Args:
        - name 基础配置文件[frameName]section下的key值或者frame名称或者id
        - default 是否跳回默认Frame,默认为True
    
    '''
    return frame.switchTo(driver, name, default)
#导航   
def navClickTop(*names):
    '''导航目前分为三级,第一级悬浮菜单项,第二级分组名称可以省略,第三级为导航节点
        
        :Args:
            - names 导航信息
    '''
    return Navigation(driver).clickTop(*names)
#页签   
def tabsClickBg(name):
    return tabs.clickBg(driver, name)

#分页
def pagingNext():
    '''                 
    '''
    return Paging(driver).next()
def pagingPrev():
    '''                 
    '''
    return Paging(driver).prev()
def pagingFirst():
    '''                 
    '''
    return Paging(driver).first()
def pagingLast():
    '''                 
    '''
    return Paging(driver).last()
def pagingNum(number):
    return Paging(driver).num(number)
def pagingCurrNum():  
    return Paging(driver).currNum()
#列表
             
def tableCheckAll(tableId = cfg.getBaseCfg("id", "bg_table")):
    Table(driver, tableId).checkAll()
def tableUncheckAll(tableId = cfg.getBaseCfg("id", "bg_table")):
    Table(driver, tableId).unCheckAll()
def tableCheckByNum(number, tableId = cfg.getBaseCfg("id", "bg_table")):
    Table(driver, tableId).checkByNum(number)

def tableUncheckByNum(number, tableId = cfg.getBaseCfg("id", "bg_table")):
    Table(driver, tableId).uncheckByNum(number)

def tableChekByContent(name, value, tableId = cfg.getBaseCfg("id", "bg_table")):
    Table(driver, tableId).chekByContent(name, value)
def tableUnchekByContent(name, value, tableId = cfg.getBaseCfg("id", "bg_table")):
    Table(driver, tableId).unchekByContent(name, value)
def tableClickByContent(name, value, clickName = "", clickColName=cfg.getBaseCfg("text", "bg_clickColName"), tableId = cfg.getBaseCfg("id", "bg_table")):
    Table(driver, tableId).clickByContent(name, value, clickName, clickColName)
def tableSelectAllCheckbox(tableId):
    SimpleTable(driver, tableId).selectAllCheckbox()
    
#赋值
def setValueByIds(idValue):
    Value(driver).byIds(idValue)
def setValueById( htmlId, value):
    Value(driver).byId(htmlId, value)
def selectValueByText(htmlId, text):
    Value(driver).selectByText(htmlId, text)
def setValueByName(name, text):
    Value(driver).byName(name, text)
def setValues(idOrNameDic, valueDic):
    '''批量赋值
        
    :Args:
        - idOrNameDic id或name组成的字典
        - valueDic值字典
    '''
    Value(driver).setValues(idOrNameDic, valueDic)
def setValuesBySection(section):
    '''批量赋值(section名称)
        
    :Args:
        - section section名称(ini组名)
    '''
    Value(driver).setValues(*cfg.getIdValueDic(section))    
    
    
def setValuesByClass(classDic, valueDic):
    '''级联赋值
        
    :Args:
        - classDic class组成的字典
        - valueDic值字典
    '''
    Value(driver).setValuesByClass(classDic, valueDic)    
    
def setValueList(htmlName, valueList):
    '''通过列表每个输入项赋不同的值
        
    :Args:
        - htmlName 控件name
        - valueList 值列表
    ''' 
    Value(driver).setValueList(htmlName, valueList)
    

def setValue(idOrName, value):
    '''赋值
        
    :Args:
        - idOrName id或name值
        - value 值
    '''
    setValues({"赋值":idOrName}, {"赋值":value})
def setCheckboxCascaded(htmlName, valueDic):
    '''级联复选框 赋值
        
    :Args:
        - htmlName 父复选框name
        - valueDic 值,格式如下{父文本1:[子文本1,子文本2], 父文本2:[子文本3,子文本4]}
    '''
    Value(driver).setCheckboxCascaded(htmlName, valueDic)
#数据字典保存
def setDataById(htmlid, key):
    SaveValue(driver).saveById(htmlid, key)
    
#同步
def overlayDisappear():
    '''同步遮罩消失
        
    :Args:
        
    '''
    Wait(driver).waitObjDisappear("overlay")
def noteDisappear():
    '''同步消息通知框消失
        
    :Args:
        
    '''
    Wait(driver).waitObjDisappear("note_item")
def noteSuccess(content = None):
    '''成功通知框验证
        
    :Args:
        - content 通知内容
    '''
    return Wait(driver).note(content, "success")
def noteError(content = None):
    '''错误通知框验证
        
    :Args:
        - content 通知内容
    '''
    return Wait(driver).note(content, "error")
def noteInfo(content = None):
    '''消息错误通知框验证
        
    :Args:
        - content 通知内容
    '''
    return Wait(driver).note(content, "info")
def noteWarn(content = None):
    '''警告通知框验证
        
    :Args:
        - content 通知内容
    '''
    return Wait(driver).note(content, "warn")
def isAlertPresent(shortTime = False):
    return Wait(driver).isAlertPresent(shortTime)

#浏览器
def closeWindow(num = 0):
    return Window(driver).closeWindow(num)