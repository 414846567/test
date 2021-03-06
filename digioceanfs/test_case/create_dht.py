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

class Create_dht(unittest.TestCase):
    def setUp(self):
	self.driver = common.browers()
        self.driver.implicitly_wait(30)
        self.base_url = common.baseurl()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_dht(self):
        driver = self.driver
	login.test_login(self)
        driver.find_element_by_link_text(u"存储服务管理").click()
	create_service=driver.find_element_by_link_text(u"创建&扩容")
	ActionChains(driver).move_to_element(create_service).perform()	
	driver.find_element_by_link_text(u"创建服务").click()
        driver.find_element_by_id("clusterservicename").clear()
        driver.find_element_by_id("clusterservicename").send_keys("test")
        driver.find_element_by_id("btnext").click()
	time.sleep(1)	
        driver.find_element_by_id("btnext").click()
        driver.find_element_by_css_selector("input[type=\"checkbox\"]").click()
        driver.find_element_by_id("btfinished").click()
	driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
	time.sleep(2)
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_css_selector("a.ui-icon.ui-icon-power").click()
	self.driver.implicitly_wait(120)
        driver.find_element_by_xpath("//button[@type='button']").click()
	time.sleep(3)
	driver.find_element_by_xpath(".//*[@id='test_tr']/td[1]/dl[1]/dd/a").click()
	driver.find_element_by_xpath(".//*[@id='ext-gen1018']/div[2]/div[3]/div/button[2]").click()
	self.driver.implicitly_wait(60)
	driver.find_element_by_xpath("//button[@type='button']").click()

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

