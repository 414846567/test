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

class Domain_set(unittest.TestCase): 
    def setUp(self):
 	self.driver = common.browers()
        self.driver.implicitly_wait(30)
        self.base_url = common.baseurl()
        self.verificationErrors = []
        self.accept_next_alert = True	
    def test_add_domain(self):
	"""设置域名"""
        driver=self.driver
	#导入登录模块
        login.test_login(self)	
	driver.find_element_by_link_text(u"存储节点管理").click()		        
	setup_domain=driver.find_element_by_link_text(u"设置")
	ActionChains(driver).move_to_element(setup_domain).perform()
        driver.find_element_by_link_text(u"设置域名").click()
        driver.find_element_by_id("clusterdomainname").clear()
        driver.find_element_by_id("clusterdomainname").send_keys("yyy")
        driver.find_element_by_id("domainnamesave").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
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
