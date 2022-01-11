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
#from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from itemURLs import urls_array
import time

#from selenium.webdriver.common.action_chains import ActionChains


def change_zip(url_check, zipzip):
    
    options = Options()
    options.headless = True

    driver = webdriver.Firefox()
    driver.implicitly_wait(0.5)
    driver.get(url_check)
    
    def tryit():
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
            #close_class = "as-overlay-close ase-overlay-close"
            b = driver.find_element_by_xpath(close_path)
            driver.execute_script("arguments[0].click();", b)
            #WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="as-overlay-close ase-overlay-close"]'))).click()
            
            
            time.sleep(5)
            return
        except StaleElementReferenceException:
            return tryit()
    
    tryit()
    driver.quit()
    return

    
zipzip = 27514
#change_zip(urls_array[0], zipzip)

def check_store(url_check):
    options = Options()
    options.headless = True

    driver = webdriver.Firefox()
    driver.implicitly_wait(0.5)
    driver.get(url_check)
    
    pathth = '//*[@id="check-availability-search-section"]/div/div/div/div/span[2]/button'
    store_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, pathth))).text
    driver.quit()
    return store_name

print(check_store(urls_array[0]))

def check_available(url_check):
    options = Options()
    options.headless = True

    driver = webdriver.Firefox()
    driver.implicitly_wait(0.5)
    driver.get(url_check)
    
    pathth = '//*[@id="check-availability-search-section"]/div/div/div/div/span[2]'
    store_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, pathth))).text
    driver.quit()
    return store_name

print(check_available(urls_array[0]))

def runner():
    options = Options()
    options.headless = True

    driver = webdriver.Firefox()
    driver.implicitly_wait(0.5)
    driver.get(urls_array[0])
    
    zipzip = 27514
    
    change_zip(urls_array[0], zipzip)
    sch = check_store(urls_array[0],zipzip)
    print(sch)
    for x in range(len(urls_array)):
        ach = change_zip(urls_array[x],zipzip)
        if ach is None:
            print("Available")
            x = x - 1
        else:
            print(ach)
    
    driver.quit()
    return

runner()
