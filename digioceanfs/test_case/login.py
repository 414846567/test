# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time,re
import common
        
def test_login(self):

     	driver = self.driver 
       	driver.get(self.base_url)
     	driver.find_element_by_id("name").clear()
     	driver.find_element_by_id("name").send_keys("admin")
     	driver.find_element_by_id("passwd").clear()
     	driver.find_element_by_id("passwd").send_keys("12345678")
     	driver.find_element_by_css_selector("input.button").click()
	time.sleep(5)
