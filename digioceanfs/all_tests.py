#coding=utf-8
#测试用例组件
import unittest
import sys,time
#报告模块
import HTMLTestRunner
#导入测试用例组
sys.path.append("test_case/")
from test_case import *
#用例数组，添加用例
alltestnames=[
	domain_set.Domain_set,
		]


testunit=unittest.TestSuite()


for test in alltestnames:
	testunit.addTest(unittest.makeSuite(test))
#testunit.addTest(unittest.makeSuite(add_node.Add_node))

#now=time.strftime('%Y-%m-%d_%H:%M',time.localtime(time.time()))
#生成测试报告
#filename="report/"+now+"_result.html"
filename="/root/report/result.html"
fp=open(filename,"wb")
runner=HTMLTestRunner.HTMLTestRunner(
	stream=fp,
	title=u'集群文件系统测试报告',
	description=u'用例执行情况：')
#runner=unittest.TextTestRunner()
#执行测试
runner.run(testunit)
