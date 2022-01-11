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

from selenium.webdriver.common.action_chains import ActionChains






def check_available(url_check, zipzip):
    
    options = Options()
    options.headless = True
    
    #<button class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink" data-autom="deliveryDateChecker" data-ase-overlay="dude-overlay" data-ase-click="show">27514</button>
    
    driver = webdriver.Firefox()
    driver.implicitly_wait(0.5)
    driver.get(url_check)
    
    #<button class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink" data-autom="deliveryDateChecker" data-ase-overlay="dude-overlay" data-ase-click="show" style="">27601†† </button>
    
    #my_path = '//input[@class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink"]'
    #my_class = "rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink"
    #css_sel = "#actiontray > div > div.toggletray > div.as-actiontray-deliverydates > div > span.as-purchaseinfo-dudeinfo-suffixlabel > button"
    #css_sel = "html.en-us.amr.js.en.seg-consumer.us.no-supports-applepay.no-supports-apw.svg.no-touch.no-ie.no-oldie.no-ios.supports-animation.supports-columns.no-supports-backdrop-filter.as-mouseuser body.cto-mac.cto-macbook-pro.black.as-theme-light-heroimage.as-buyflowmessages-acmienabled.rs-configurations-acmifinancepresent div#page.as-cto-page div div form#configuration-form div#actiontray.as-actiontray.sticky-actiontray.as-buyflow-messages-hidedefaultfinancing.rs-configurations-actiontrayready.change div.as-l-container div.toggletray div.as-actiontray-deliverydates div.as-purchaseinfo-dudeinfo-dude2 span.as-purchaseinfo-dudeinfo-suffixlabel button.rf-dude-quote-overlay-trigger.as-delivery-overlay-trigger.as-purchaseinfo-dudetrigger.as-buttonlink"
    #element = driver.find_element_by_css_selector(css_sel)
    pathpath = '/html/body/div[2]/div[8]/div[1]/form/div[3]/div/div[1]/div[1]/div/span[2]/button'
    #element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, pathpath)))
    #css_sel = '.rf-dude-quote-overlay-trigger'
    def tryit():
        try:
            #Finds Zipcode Button and clicks it
            #element1 = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, pathpath)))
            b = driver.find_element_by_xpath(pathpath)
            driver.execute_script("arguments[0].click();", b)
            
            element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, pathpath)))
            element.click()
            time.sleep(10)
            return
        except StaleElementReferenceException:
            return tryit()
    #print(len(element))
    tryit()
    time.sleep(2)
    
   #WebDriverWait(driver, 10).until(EC.visibility_of_elements_located((By.XPATH, '//button[@class="rf-pickup-quote-overlay-trigger as-retailavailabilitytrigger-infobutton retail-availability-search-trigger as-buttonlink"]'))).click()
    '''
    
    #my_path = '//button[@class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink"]'
    #ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    #WebDriverWait(driver, 2,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, my_path))).click()
    
    #element = driver.find_element_by_class("rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink")
    #driver.execute_script("arguments[0].scrollIntoView();", element)
    
    #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="rf-pickup-quote-overlay-trigger as-retailavailabilitytrigger-infobutton retail-availability-search-trigger as-buttonlink"]'))).click()
    
    zipcode_input = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ii_searchreset"]')))
    
    zipcode_input.clear()
    zipcode_input.send_keys(str(zipzip))
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="as-retailavailabilitysearch-searchbutton"]'))).click()
    
    
    avail_text = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="as-storeitem-indicatortext large-12 small-6 column as-retailavailability-text ships-to-store "]')))
    availability = avail_text.text
    '''
    driver.quit()
    return True

    
zipzip = 27514
ach = check_available(urls_array[0], zipzip)
print(ach)

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
        if ach is None:
            print("Available")
            x = x - 1
        else:
            print(ach)


#runner()
