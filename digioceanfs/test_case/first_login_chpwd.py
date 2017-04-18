# -*- coding: utf-8 -*-
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

class First_login_chpwd(unittest.TestCase): 
    def setUp(self):
 	self.driver = common.browers()
        self.driver.implicitly_wait(30)
        self.base_url = common.baseurl()
        self.verificationErrors = []
        self.accept_next_alert = True	
    def test_add_domain(self):
	"""第一次登陆修改密码"""
        driver=self.driver
	#导入登录模块
        login.test_login(self)	
	driver.find_element_by_id("old_password").clear()
        driver.find_element_by_id("old_password").send_keys("12345678")
        driver.find_element_by_id("new_password").clear()
        driver.find_element_by_id("new_password").send_keys("12345678")
        driver.find_element_by_id("confirm_new_password").clear()
        driver.find_element_by_id("confirm_new_password").send_keys("12345678")
        driver.find_element_by_xpath(".//*[@id='ext-gen1018']/div/div[3]/div/button").click()
		
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
