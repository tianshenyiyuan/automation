# encoding=utf-8
'''
Created on 2016年9月12日

@author: kun.wang
'''

from testcase import testcase1
from unittest.suite import TestSuite
import os
import unittest
test_cases = (testcase1.Testcase1, )

def load_tests(loader, tests):
    suite = TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite

def load_tests2(loader, standard_tests, pattern):
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests
loader = unittest.defaultTestLoader
#unittest.TextTestRunner(stream=open("d:\\a.log", "w+" )).run( loader.loadTestsFromTestCase(testcase1.Testcase1))
unittest.TextTestRunner(stream=open("d:\\a.log", "w+" )).run( load_tests(loader, test_cases))