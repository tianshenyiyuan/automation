# encoding: utf-8
'''
Created on 2016年5月21日

@author: 弈远
'''
# from common.code import function
from common.code.function.element import Element
def getAllId(driver, element = None):
    """获取页面所有控件的id
    :Args
        -driver driver
        -element 对象
    """
    driverOrEle = driver if element == None else element
    idLIst = []
    elements = driverOrEle.find_elements_by_xpath(".//input[(@type='text' or @type='password') or @type='radio' or @type='checkbox' or @type='file'  or @type='image'] | .//select| .//textarea")        
    names = ""
    for ele in elements:
        id = ele.get_attribute('id')
        #id重复的只保存第一个
        if not id in idLIst:
            idLIst.append(id)
            getEleObj = Element(driver)
            try:
                name = driver.execute_script("return arguments[0].innerText", getEleObj.previousSibling(getEleObj.parent(ele))).strip()
            except:
                name = ""
            if name.endswith("：") or name.endswith(":") : #去掉冒号
                name = name[0:len(name) - 1]
            print name , "=" ,id
            names = names + name + " = \n"
    print names
        


#     elements = driver.find_elements_by_tag_name("label")
#     i = 0
#     for ele in elements:
#         #name = ele.text
#         #隐藏的情况下text取值为空
#         name = driver.execute_script("return arguments[0].innerText", ele).strip()
#         if name == "" :
#             name = "是空这可怎么办%d" % i
#             i = i + 1
#         if name.endswith("：") or name.endswith(":") : #去掉冒号
#             name = name[0:len(name) - 1]
#         print name , "=" , ele.get_attribute("for")





#         try:
#             inputEle = function.nextSibling(ele)
#         except:
#             #没有获取到时,通过父节点的兄弟节点的第一个子节点
#             inputEle = function.parent(ele)  
#             inputEle = function.nextSibling(inputEle)
#             inputEle = function.firstChild(inputEle)
#         if inputEle.tag_name == 'div' : #div为富文本框特殊处理
#             try:
#                 htmlId = driver.execute_script("return arguments[0].firstChild.getAttribute('id')", inputEle)
#             except: #不可处理的div直接跳过
#                 pass
#         else:
#             htmlId = inputEle.get_attribute("id").strip()
#         
#         onfocus = inputEle.get_attribute("onfocus")
#         if onfocus!=None and onfocus.startswith("WdatePicker"): #时间控件分开始和结束需要特殊处理
#             print name , "=" , htmlId if htmlId else inputEle.get_attribute("name").strip()
#             try:
#                 inputEle = function.nextSibling(inputEle)
#                 if inputEle.tag_name != "input":
#                     inputEle = function.nextSibling(inputEle)
#                 if inputEle.tag_name == "input":
#                     htmlId = inputEle.get_attribute("id").strip()
#                     print name + "结束", "=" , htmlId if htmlId else inputEle.get_attribute("name").strip()
#             except Exception:
#                 pass
#         else:
#             print name , "=" , htmlId if htmlId else inputEle.get_attribute("name").strip() if inputEle.get_attribute("name") else ""
#     
#     #商品简称：