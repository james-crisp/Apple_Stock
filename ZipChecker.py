#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:00:41 2022

@author: jimmycrisp
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from itemURLs import urls_array
import time

def check_available(url_check, zipzip):
    options = Options()
    options.headless = True
    
    driver = webdriver.Firefox()
    driver.implicitly_wait(0.5)
    
    driver.get(url_check)
   
    button = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="rf-pickup-quote-overlay-trigger as-retailavailabilitytrigger-infobutton retail-availability-search-trigger as-buttonlink"]')))
    time.sleep(1)
    button.click()
    
    zipcode_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ii_searchreset"]')))
    
    zipcode_input.clear()
    zipcode_input.send_keys(str(zipzip))
    search_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="as-retailavailabilitysearch-searchbutton"]')))
    search_button.click()
    
    store_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="as-storeitem-info small-12 column"]')))
    
    print(store_text.text)
    
    avail_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="as-storeitem-indicatortext large-12 small-6 column as-retailavailability-text ships-to-store "]')))
    print(avail_text.text)
    
    driver.quit()
    
    return

    

def runner():
    zipzip = 27514
    for x in range(len(urls_array)):
        check_available(urls_array[x],zipzip)

runner()
