# encoding=utf-8
'''
Created on 2016年5月23日

@author: 弈远
'''
import time
import random
def parser(value):
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
        tempValue = _expressionParse(value[leftBrace + 1:rightBrace])
        
        leftStr = value[0:leftBrace] + tempValue
        if rightBrace == len(value) - 1:
            return leftStr
        else:
            rightStr = value[rightBrace + 1:]
    
    return leftStr + parser(rightStr) #递归
def _expressionParse(value):
    if value in ["今天","date","Date"]:
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
    else:
        return value