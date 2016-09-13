# encoding: utf-8
#获取配置信息
import os
baseDir = os.path.split(os.path.realpath(__file__))[0]
cfgDir = baseDir + "/../cfg/" 
logDir = baseDir + "/../log/"
picDir = baseDir + "/../pic/" 
picDir = picDir.replace("/", os.path.sep).replace("\\", os.path.sep)