import unittest
from utils.HTMLTestRunner import HTMLTestRunner
from login_testcase import XXLoginTest


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(XXLoginTest))

with open('./reports/XX_login_test_report.html', 'wb') as f:
    h = HTMLTestRunner(stream=f, title='XX登陆自动测试化报告', description='window chrome')
    h.run(suite)
