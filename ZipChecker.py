#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:00:41 2022

@author: jimmycrisp
"""
# Main Webdriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# Exceptions
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


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
    
    def refresh():
        try:
            my_path = '//button[@class="rf-pickup-quote-overlay-trigger as-retailavailabilitytrigger-infobutton retail-availability-search-trigger as-buttonlink"]'
            ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
            WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, my_path))).click()
    
            #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="rf-pickup-quote-overlay-trigger as-retailavailabilitytrigger-infobutton retail-availability-search-trigger as-buttonlink"]'))).click()
    
            zipcode_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ii_searchreset"]')))
    
            zipcode_input.clear()
            zipcode_input.send_keys(str(zipzip))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="as-retailavailabilitysearch-searchbutton"]'))).click()
    
    
            avail_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="as-storeitem-indicatortext large-12 small-6 column as-retailavailability-text ships-to-store "]')))
            availability = avail_text.text
    
            driver.quit()
            return availability
    
        except:
            driver.quit()
            driver.get(url_check)
            refresh()
            
    ans = refresh()
    return ans


def check_store(url_check, zipzip):
    
    options = Options()
    options.headless = True
    
    driver = webdriver.Firefox()
    driver.implicitly_wait(0.5)
    
    driver.get(url_check)
    
    my_path = '//button[@class="rf-pickup-quote-overlay-trigger as-retailavailabilitytrigger-infobutton retail-availability-search-trigger as-buttonlink"]'
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, my_path))).click()
    
    #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="rf-pickup-quote-overlay-trigger as-retailavailabilitytrigger-infobutton retail-availability-search-trigger as-buttonlink"]'))).click()
    
    zipcode_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ii_searchreset"]')))
    
    zipcode_input.clear()
    zipcode_input.send_keys(str(zipzip))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="as-retailavailabilitysearch-searchbutton"]'))).click()
    
    
    store_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="as-storeitem-info small-12 column"]')))
    
    stored = store_text.text
    
    driver.quit()
    return stored


def runner():
    zipzip = 27514
    sch = check_store(urls_array[0],zipzip)
    print(sch)
    for x in range(len(urls_array)):
        ach = check_available(urls_array[x],zipzip)
        print(ach)


runner()
