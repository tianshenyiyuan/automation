# encoding: utf-8
'''
Created on 2016年5月9日

@author: 弈远
'''
import os,time
from common import logDir
class WriteLog(object):
    '''
             记录日志
    '''
#     basePath = os.path.split(os.path.realpath(__file__))[0] + "../../../../log/"
    runtimePath = logDir + "Runtime.log"
    errorPath = logDir + "Error.log"
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    runtimeFile = open(os.path.abspath(runtimePath), "a")
    errorFile = open(os.path.abspath(errorPath), "a")

    def __init__(self, params):
        '''
        Constructor
        '''
    @staticmethod
    def logError(msg):
        WriteLog.__log('error', msg)
    @staticmethod
    def logWarn(msg):
        WriteLog.__log('warn', msg)
    @staticmethod
    def logDone(msg):
        WriteLog.__log('done', msg)
    @staticmethod
    def logPass(msg):
        WriteLog.__log('pass', msg)
    
    @staticmethod    
    def GetNowTime():
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    
    @staticmethod    
    def __log(logType, msg):
        if logType == "error":
            WriteLog.__write(WriteLog.errorFile, logType, msg)
        WriteLog.__write(WriteLog.runtimeFile, logType, msg)
    @staticmethod    
    def __write(writeFile, logType, msg):
        writeFile.writelines(WriteLog.GetNowTime() + ": [" + logType + "]" + msg + '\n')
def logError(msg):
        WriteLog.logError(msg)
def logWarn(msg):
        WriteLog.logWarn(msg)
def logPass(msg):
        WriteLog.logPass(msg)
def logDone(msg):
        WriteLog.logDone(msg)