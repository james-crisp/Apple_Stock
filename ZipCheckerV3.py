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
#from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from itemURLs import urls_array
import time

#from selenium.webdriver.common.action_chains import ActionChains


def change_zip(driver,zipzip):
    try:
        #Finds Zipcode Button and clicks it
        pathpath = '/html/body/div[2]/div[8]/div[1]/form/div[3]/div/div[1]/div[1]/div/span[2]/button'
        b = driver.find_element_by_xpath(pathpath)
        driver.execute_script("arguments[0].click();", b)
        
        zipcode_input = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="postalCode"]')))
        
        zipcode_input.clear()
        zipcode_input.send_keys(str(zipzip))
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="as-deliverydatesoverlay-addressform-button button merchandising"]'))).click()
        
        close_path = '/html/body/overlay[14]/materializer/div/div/button'
        b = driver.find_element_by_xpath(close_path)
        driver.execute_script("arguments[0].click();", b)
    
    except StaleElementReferenceException:
        time.sleep(1)
        return change_zip(driver,zipzip)
    
    #time.sleep(5) error checking
    return

def check_store(driver):
    try:
        pathth = '//*[@id="check-availability-search-section"]/div/div/div/div/span[2]/button'
        store_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, pathth))).text
    except TimeoutException:
        driver.refresh()
        return check_store(driver)
        
    return store_name


def check_available(driver):
    try:
        #pathth = '//*[@id="check-availability-search-section"]/div/div/div/div/span[2]'
        #pathth = '//*[@id="check-availability-search-section"]/div/div/div/div/span[2]/span'
        #pathth = '//*[@id="check-availability-search-section"]/div/div/div/div/span[2]/text()'
        time.sleep(1)
        pathth = '//*[@id="check-availability-search-section"]/div/div/div/div/span[2]'
        #classy ="as-retailavailabilitytrigger-value"
        #classy ="as-pickup-quote-availability-quote"
        check_item = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, pathth))).text
        #check_item = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, classy))).text
        #driver.refresh()
        #check_item = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, classy))).text
        #time.sleep(1)
    except (TimeoutException, StaleElementReferenceException):
        time.sleep(1)
        driver.refresh()
        return check_available(driver)
        
    return check_item


def runner():
    options = Options()
    options.headless = True

    driver = webdriver.Firefox()
    driver.implicitly_wait(0.5)
    driver.get(urls_array[0])
    
    zipzip = 27514
    
    change_zip(driver,zipzip)
    time.sleep(1)
    driver.refresh()
    print(check_store(driver))
    for x in range(0,len(urls_array)):
        time.sleep(1)
        driver.get(urls_array[x])
        print(check_available(driver))
    
    driver.quit()
    
    return

runner()
