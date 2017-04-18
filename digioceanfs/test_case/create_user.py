#coding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
import common
import login

class Create_user(unittest.TestCase):
    def setUp(self):
	self.driver = common.browers()
        self.driver.implicitly_wait(30)
        self.base_url = common.baseurl()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_user(self):
        driver = self.driver
	login.test_login(self)
	driver.find_element_by_link_text(u"存储服务管理").click()
	setup_service=driver.find_element_by_link_text(u"服务配置")	
	ActionChains(driver).move_to_element(setup_service).perform()	
        driver.find_element_by_link_text(u"共享用户和组").click()
	self.driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"新建用户").click()
        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys("caoyi")
        driver.find_element_by_id("comment").clear()
        driver.find_element_by_id("comment").send_keys("caoyi")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("authpassword").clear()
        driver.find_element_by_id("authpassword").send_keys("123456")
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//table[@id='tblusers']/tbody/tr/td/dl/dd[2]/a").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
	
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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

