# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
import sys,os

SN=[]
class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "10.10.16.22"
        self.verificationErrors = []
        self.accept_next_alert = True

        
    def test_login(self):
        driver = self.driver
        driver.get("https://"+self.base_url + "/login?redirect_url=/")
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("admin")
        driver.find_element_by_id("passwd").clear()
        driver.find_element_by_id("passwd").send_keys("12345678")
        driver.find_element_by_css_selector("input.button").click()
        self.driver.implicitly_wait(10)
        
        driver.find_element_by_link_text(u"注册License").click()
        self.driver.implicitly_wait(10)
	driver.find_element_by_id("set_sn").send_keys(sn)
	driver.find_element_by_id("set_sn_button").click()
	self.driver.implicitly_wait(10)
	check_tag=driver.find_element_by_xpath(".//*[@id='content']/fieldset/span[5]").text	
	print check_tag
#        ActionChains(driver).move_to_element(admin).perform()
#        driver.find_element_by_class_name("sub_menu_1").find_element_by_link_text(u"修改密码")
#	driver.find_element_by_id("old_password").clear()
#        driver.find_element_by_id("old_password").send_keys("12345678")
#        driver.find_element_by_id("new_password").clear()
#        driver.find_element_by_id("new_password").send_keys("12345678")
#        driver.find_element_by_id("confirm_new_password").clear()
#        driver.find_element_by_id("confirm_new_password").send_keys("12345678")
#        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
 #       driver.find_element_by_link_text(u"注册license").click()
 #       admin=driver.find_element_by_xpath("/html/body/element/div[1]/dl/ul/li[2]/span")
 #       ActionChains(driver).move_to_element(admin).perform()
 #       driver.find_element_by_class_name("sub_menu_1").find_element_by_link_text(u"退出").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
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
    
 #   def tearDown(self):
 #       self.driver.quit()
 #       self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
#    s=raw_input("please input IPADDR:")	
    sn=raw_input("please input sn:")	
    unittest.main()
