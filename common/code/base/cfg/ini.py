# encoding: utf-8
'''
Created on 2016年5月9日

@author: 弈远
'''
import ConfigParser, os
import random, time
import codecs
import sys
from common import cfgDir
from ConfigParser import NoOptionError
from collections import OrderedDict
from common.code.base import data, log
import itertools
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
#将配置内容进行缓存(读写内容很多只对读取做缓存)
cache = {}
def getValue(fileName, section, key, default = ""):
    return iniHelper(fileName).getValue(unicode(section), unicode(key), unicode(default))
def setValue(fileName, section, key, value):
    return iniHelper(fileName).setValue(unicode(section), unicode(key), unicode(value))
def getDic(fileName, section):
    return iniHelper(fileName).getDic(unicode(section))
class iniHelper(object):
    def __init__(self, filename):
        #处理filename为绝对路径
        filename = unicode(filename)
        if os.path.exists(filename):
            self.filename = unicode(filename)
        else:
            self.filename = unicode(cfgDir) + unicode(filename)
        
        self.initflag = False
        self.cfg = None
        self.readhandle = None
        self.writehandle = None
    def init(self):
        self.cfg = ConfigParser.ConfigParser()
        try:
            if self.filename in cache:
                self.readhandle = cache[self.filename] 
            else:
                self.readhandle = self._getReadhandle()                
            self.cfg.readfp(self.readhandle)
            #self.writehandle = open(self.filename, 'w')
            self.initflag = True
        except IOError,msg:
            print msg
            self.initflag = False
        return self.initflag
    def unInit(self):
        if self.initflag:
            #self.readhandle.close() 读取流不关闭
            self.writehandle.close()
    def getValue(self, Section, Key, Default = ""):
        if not self.initflag:
            self.init()
        try:
            Section = self._getSection(Section)
            value = self._parser(self.cfg.get(Section, Key))
        except NoOptionError:
            #log.logWarn(msg)
            value = Default
        return value
    def setValue(self, Section, Key, Value):
        Section = self._getSection(Section)
        if not self.initflag:
            self.init()
        try:
            self.cfg.set(Section, Key, Value)
        except:
            self.cfg.add_section(Section)
            self.cfg.set(Section, Key, Value)
        try:
            writeFile = codecs.open(self.filename, 'w', "utf-8-sig")
        except UnicodeDecodeError:
            writeFile =  codecs.open(self.filename, 'w') #非utf-8文件使用默认方式
        finally:
            self.cfg.write(writeFile)
            writeFile.close()           
        #更新读取catch和读取文件
        self.readhandle = self._getReadhandle()
        if self.filename in cache:
            cache[self.filename] = self.readhandle 
    def getDic(self, section):
        dic = OrderedDict() #按顺序显示
        if not self.initflag:
            self.init()
        for item in self.cfg.items(self._getSection(section)):
            dic[item[0]] = self._parser(item[1])
        return dic        
    def _getSection(self, name):
        caseName = data.getData("用例名")
        if None == caseName or "" == caseName.strip():
            return name
        if not self.initflag:
            self.init()
        
        nameSplit = caseName.split("_")
        #组合数的匹配
        for i in range(len(nameSplit), 0, -1):
            for nameList in itertools.combinations(nameSplit, i):
                nameJoin = reduce(lambda x, y : x + "_" + y, nameList) + "_" + name
                if self.cfg.has_section(nameJoin):
                    return nameJoin
        return name
       
    def _getReadhandle(self):
        try:
            return  codecs.open(self.filename, 'r', "utf-8-sig")
        except UnicodeDecodeError:
            return  codecs.open(self.filename, 'r') #非utf-8文件使用默认方式

    def _parser(self, value):
        try:
            leftBrace = value.index("{")
            rightBrace = value.index("}")
        except ValueError:
            return value
        if leftBrace > rightBrace:
            leftStr = value[0:leftBrace]
            rightStr = value[leftBrace:]
        elif rightBrace - leftBrace == 1:
            leftStr =  value[0:leftBrace]
            rightStr = value[rightBrace + 1:]
        else:
            tempValue = self._expressionParse(value[leftBrace + 1:rightBrace])
            
            leftStr = value[0:leftBrace] + tempValue
            if rightBrace == len(value) - 1:
                return leftStr
            else:
                rightStr = value[rightBrace + 1:]
        
        return leftStr + self.parser(rightStr) #递归
    def _expressionParse(self, value):
        if "." in value:
            values = value.split("." )
            if len(values) == 3:
                if unicode(values[0]) == unicode("配置"):
                    return getValue("cfg.ini", values[1], values[2])
                else:
                    return value
            elif len(values) == 2:
                if unicode(values[0]) == unicode("配置"):
                    return getDic("cfg.ini", values[1])
                else:
                    return value
            else:
                return value
        elif value in ["今天","date","Date"]:
            return str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        elif value in ["现在","now","Now"]:
            return str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        elif value.startswith("随机数"):
            values = value.split(",")
            if len(values) == 1:
                length = 4 #默认生成四位随机数
            length = int(values[1].strip())
            tempValue = str(random.randint(0, 10**length - 1))
            tempValue = "0" * (length - len(tempValue)) + tempValue        
            return tempValue
        if value in ["时间戳","timestamp","Timestamp"]:
            return str(int(time.time()*1000) )
        else:
            return value
        