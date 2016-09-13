# encoding=utf-8
'''
Created on 2016年7月8日

@author: 弈远
'''
from common.code.function import wait
class Window(object): 
    def __init__(self, driver):
        self.driver = driver
        '''
        Constructor
        '''   
    def closeWindow(self, num = 0):
        handle = self.driver.current_window_handle
        wait.windowCount(self.driver, num)
        self.driver.switch_to.window(self.driver.window_handles[num])
        self.driver.close()
        #返回原handle
        if num != 0:
            self.driver.switch_to.window(handle)
        