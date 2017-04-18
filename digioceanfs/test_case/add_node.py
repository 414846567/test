#coding=utf-8
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

class Add_node(unittest.TestCase):
    def setUp(self):
        self.driver = common.browers()
        self.driver.implicitly_wait(30)
        self.base_url = common.baseurl()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_node(self):
        driver=self.driver
        login.test_login(self)
        driver.find_element_by_link_text(u"存储节点管理").click()
        with file("../test_data/node_list_file") as f:
            ips=f.readlines()
            for ip in ips:
                node_mgmt=driver.find_element_by_class_name("toolbar-menu")
                ActionChains(driver).move_to_element(node_mgmt).perform()
                driver.find_element_by_link_text(u"添加存储节点").click()
                driver.find_element_by_id("clusternodeipaddr_octet_1").clear()
                driver.find_element_by_id("clusternodeipaddr_octet_1").send_keys(ip.split('.')[0])
                driver.find_element_by_id("clusternodeipaddr_octet_2").clear()
                driver.find_element_by_id("clusternodeipaddr_octet_2").send_keys(ip.split('.')[1])
                driver.find_element_by_id("clusternodeipaddr_octet_3").clear()
                driver.find_element_by_id("clusternodeipaddr_octet_3").send_keys(ip.split('.')[2])
                driver.find_element_by_id("clusternodeipaddr_octet_4").clear()
                driver.find_element_by_id("clusternodeipaddr_octet_4").send_keys(ip.split('.')[3])
                driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
                driver.find_element_by_xpath("//button[@type='button']").click()

    def is_element_present(self, how, what):
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
