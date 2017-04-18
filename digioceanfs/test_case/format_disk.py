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

class Format_disk(unittest.TestCase):

    def setUp(self):
	self.driver = common.browers()
        self.driver.implicitly_wait(30)
        self.base_url = common.baseurl()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_format_disk(self):
	"""格式化磁盘"""
        driver = self.driver
	login.test_login(self)
        driver.find_element_by_link_text(u"存储服务管理").click()
	self.driver.implicitly_wait(10)
	disk_mgmt=driver.find_element_by_link_text(u"磁盘管理")
	ActionChains(driver).move_to_element(disk_mgmt).perform()
	time.sleep(1)
	driver.find_element_by_xpath(".//*[@id='toolbar']/ul/li[3]/ul/li/a").click()	
	
	driver.find_element_by_xpath(".//*[@id='disktable']/thead/tr/th[1]/div/input").click()
	disk_mgmt=driver.find_element_by_link_text(u"磁盘操作")
        ActionChains(driver).move_to_element(disk_mgmt).perform()	
	driver.find_element_by_link_text(u"格式化磁盘").click()
	
	driver.find_element_by_xpath("(//button[@type='button'])[2]").click
	self.driver.implicitly_wait(30)
	driver.find_element_by_xpath("(//button[@type='button'])").click	
	
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

