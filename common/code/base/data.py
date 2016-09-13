# encoding=utf-8
'''
Created on 2016年5月23日

@author: 弈远
'''
dataDic = {}
def getData(key):
    return dataDic.get(unicode(key))
def setData(key, value):
    dataDic[unicode(key)] = unicode(value)
        