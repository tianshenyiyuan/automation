# encoding=utf-8
'''
Created on 2016年06月22日

@author: 弈远
'''
from common.code.base import cfg
from common.code import function
moduleDic = {#模块配置
             u"示例模块":[".xx.xx.xx", "ClassName"],
    
             }  

def getModule(name):
    """
    module获取
    :Args:
        -name 模块名称
    """
    if moduleDic.has_key(unicode(name)):
        moduleValue = moduleDic[unicode(name)]
        exec "from %s import %s as moduleElement" % (moduleValue[0], moduleValue[1])
        return eval("moduleElement()")
    else:
        return None
