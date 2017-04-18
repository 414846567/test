# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time,re

class Login(unittest.TestCase):

    def setUp(self):
	u"""管理系统登录 """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.10.36.36"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_login(self):
    	try:
     	   driver = self.driver
     	   driver.get(self.base_url)
     	   driver.find_element_by_id("name").clear()
     	   driver.find_element_by_id("name").send_keys("admin")
     	   driver.find_element_by_id("passwd").clear()
     	   driver.find_element_by_id("passwd").send_keys("12345678")
     	   driver.find_element_by_css_selector("input.button").click()
#     	   self.driver.implicitly_wait(30)
	   time.sleep(10)
#     	   tt=driver.find_element_by_id("current").text
#     	   self.assertEqual(u"集群总览",tt,msg="登录失败！")
 	except AssertionError,msg:
	   print msg       
#     driver.get_screenshot_as_file("/tmp/selenium/error_png.png")
#	print	driver.find_element_by_id("log").text
  #      driver.find_element_by_link_text(u"修改密码").click()
  #      driver.find_element_by_id("old_password").clear()
  #    driver.find_element_by_id("new_password").clear()
 #     driver.find_element_by_id("new_password").send_keys("12345678")
#        driver.find_element_by_id("confirm_new_password").clear()
##        driver.find_element_by_id("confirm_new_password").send_keys("12345678")
#        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        
 #       driver.find_element_by_link_text(u"注册license").click()
 #       admin=driver.find_element_by_xpath("/html/body/element/div[1]/dl/ul/li[2]/span")
 #       ActionChains(driver).move_to_element(admin).perform()
 #       driver.find_element_by_class_name("sub_menu_1").find_element_by_link_text(u"退出").click()
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
