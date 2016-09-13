# encoding=utf-8
'''
Created on 2016年5月12日

@author: 弈远
'''

class Element(object): 
    def __init__(self, driver=None):
        self.driver = driver
        '''
        Constructor
        '''   
    def byText(self, text, basePath=""):
        if basePath == None or basePath == "":
            basePath = "//*"
        return self.driver.find_element_by_xpath(basePath + "[contains(text(),'" + str(text) + "')]")
    def nextSibling(self,element):
        return element.find_element_by_xpath("./following-sibling::*")
    def parent(self,element):
        return element.find_element_by_xpath("./parent::*")
    def previousSibling(self,element):
        return element.find_element_by_xpath("./preceding-sibling::*[1]")
    def firstChild(self,element):
        return element.find_element_by_xpath("./child::*[1]")
    def lastChild(self,element):
        return element.find_element_by_xpath("./child::*[last()]")
    def allChild(self,element):
        return element.find_elements_by_xpath("./child::*")
    def child(self,element, index):
        return element.find_element_by_xpath("./child::*[" + index + "]")
def byText(driver, text, basePath=""):  
    return Element(driver).byText(text, basePath)      
def nextSibling(element):
    return Element().nextSibling(element)
def parent(element):
    return  Element().parent(element)
def previousSibling(element):
    return  Element().previousSibling(element)
def firstChild(element):
    return  Element().firstChild(element)
def laseChild(element):
    return  Element().laseChild(element)
def allChild(element):
    return  Element().allChild(element)
def child(element, index):
    return  Element().child(element,index)