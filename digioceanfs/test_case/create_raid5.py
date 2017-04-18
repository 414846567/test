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

class Create_raid(unittest.TestCase):
    def setUp(self):
	self.driver = common.browers()
        self.driver.implicitly_wait(30)
        self.base_url = common.baseurl()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_raid(self):
	"""raid5创建"""
        driver = self.driver
	login.test_login(self)
        driver.find_element_by_link_text(u"存储服务管理").click()
	self.driver.implicitly_wait(10)
	disk_mgmt=driver.find_element_by_link_text(u"磁盘管理")
	ActionChains(driver).move_to_element(disk_mgmt).perform()
	time.sleep(1)
	driver.find_element_by_xpath(".//*[@id='toolbar']/ul/li[3]/ul/li/a").click()

	driver.find_element_by_css_selector("#disktable_filter > label > input[type=\"search\"]").send_keys("node-1.yyy")	
	driver.find_element_by_xpath(".//*[@id='disktable']/thead/tr/th[1]/div/input").click()	
	raid_mgmt=driver.find_element_by_link_text(u"RAID操作")
        ActionChains(driver).move_to_element(raid_mgmt).perform()	
	driver.find_element_by_link_text(u"创建RAID").click()
	Select(driver.find_element_by_id("clusterraidlv")).select_by_visible_text(u"RAID5")
	time.sleep(1)	
	driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
	self.driver.implicitly_wait(60)
	driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
	#更新磁盘
	time.sleep(2)	
	driver.find_element_by_xpath(".//*[@id='btclusternodedisk_update']").click()
	self.driver.implicitly_wait(10)
	driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
	#删除操作
	time.sleep(5)	
	driver.find_element_by_id("disktable").find_element_by_xpath(".//*[@id='node-1.yyy_md10']/td[2]/dl/dd/a").click()		
	self.driver.implicitly_wait(5)
	driver.find_element_by_xpath(".//*[@id='ext-gen1018']/div[3]/div[3]/div/button[2]").click()		
	self.driver.implicitly_wait(60)
	driver.find_element_by_xpath(".//*[@id='ext-gen1018']/div[2]/div[3]/div/button").click()
	
	
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

