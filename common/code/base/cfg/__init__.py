# encoding: utf-8
'''
Created on 2016年5月9日

@author: 弈远
'''
from common.code.base.cfg.ini import iniHelper
from common.code.base.cfg import ini
from common import cfgDir
from common.code.base import data
dataPath = cfgDir
def setCfgDir(name):
    global dataPath
    dataPath = name + "/"
def getBaseCfg(section, key):
    return ini.getValue("基础.ini", section, key)
def getCfg(section, key):
    return ini.getValue("配置.ini", section, key)
def getIdValueDic(section, path = "", idFileName = "控件.ini", valueFileName = "数据.ini"):
    path = _getPath(path)
    return ini.getDic(path + idFileName, section), ini.getDic(path + valueFileName, section)


def getIdDic(section, path = "", idFileName = "控件.ini"):
    path = _getPath(path)
    return ini.getDic(path + idFileName, section)

def getValueDic(section, path = "", valueFileName = "数据.ini"):
    path = _getPath(path)
    return ini.getDic(path + valueFileName, section)

def getId(section, key, path = "", idFileName = "控件.ini"):
    path = _getPath(path)
    return ini.getValue(path + idFileName, section, key)
def getValue(section, key, path = "", valueFileName = "数据.ini"):
    path = _getPath(path)
    return ini.getValue(path + valueFileName, section, key)
def _getPath(path):
    return dataPath if path == None or path.strip() == "" else path if path.replace("\\", "/").endswith("/") else path + "/"
def getData(name):
    return data.getData(name)
def setData(name, value):
    data.setData(name, value)
    
#注解(装饰器)
def caseName(name): 
    '''设置测试用例名称
    :Args:
        - name 名称
    '''
    def _call_(method):
        def _call_(*args):
            print "用例：%s 开始执行" % name
            setData('用例名',name)
            returnValue = method(*args)
            setData('用例名',"") #执行完毕后用例名清空
            print "用例：%s 执行完毕" % name
            return returnValue
        return _call_       
    return _call_   
# def cfgDir(path):
#     '''设置数据路径
#     :Args:
#         - path 路径
#     '''
#     def _call_(name):
#         setCfgDir(path)
#         return name
#     return _call_  