#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re,sys
import common
import login

class Set_license(unittest.TestCase): 
    def setUp(self):
 	self.driver = common.browers()
        self.driver.implicitly_wait(30)
        self.base_url = common.baseurl()
	self.lic_url=common.lic_url()
        self.verificationErrors = []
        self.accept_next_alert = True	
    def test_test_license(self):
	"""配置license需要在节点添加完成之后执行"""
        driver=self.driver
	#导入登录模块
	login.test_login(self)
	driver.find_element_by_link_text(u"管理License").click()
	driver.find_element_by_name("licensetable_length").click()
	driver.find_element_by_xpath(".//*[@id='licensetable_length']/label/select/option[4]").click()
	f=len(file("../test_data/node_list_file","r").readlines())
	time.sleep(2)
	for node in range(f):
		node_id="node-"+str(int(node+1))+".yyy_lic_status"	
		driver.find_element_by_id(node_id).click()
	#driver.find_element_by_id("").click()
    def is_element_present(self,how,what):
        try: self.driver.find_element(by=how,value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main() 
"""
	testunit=unittest.TestSuite()
	testunit.addTest(Domain_set("test_add_domain"))
	filename ="/root/report/report.html"
	fp =file(filename,"wb")
	runner =HTMLTestRunner,HTMLTestRunner(
		stream=fp,
		title=u'digiocean test report',
		description=u'test result:')
	runner.run(testunit)
	fp.close()
"""
