#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:00:41 2022

@author: jimmycrisp
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 09:49:45 2022

@author: jimmycrisp
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests as rq
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options)

#<button class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink" data-autom="deliveryDateChecker" data-ase-overlay="dude-overlay" data-ase-click="show">27514</button>
#<button class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink" data-autom="deliveryDateChecker" data-ase-overlay="dude-overlay" data-ase-click="show">27601†† </button>
def check_available(url_check):
    options = Options()
    options.headless = True
    #driver = webdriver.Firefox(options=options)
    #driver = webdriver.Firefox()
    driver = webdriver.Firefox()
    driver.implicitly_wait(0.5)
    #driver.maximize_window()
    driver.get(url_check)
    #Click to change zipcode
    #wait = WebDriverWait(driver, 10)
    #button = driver.find_element_by_class_name("rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink")
    #button.click()
    
    #wait = WebDriverWait(driver, 100)
    #age = wait.until(EC.visibility_of_element_located((driver.find_element_by_class_name("as-purchaseinfo-dudeinfo-label"))))
    #age.click()
    
    #button = driver.find_element_by_class_name("as-purchaseinfo-dudeinfo-label")
    #button.click()
    
    #button = driver.find_element(By.CSS_SELECTOR("#actiontray > div > div.toggletray > div.as-actiontray-deliverydates > div > span.as-purchaseinfo-dudeinfo-suffixlabel > button"))
    #button.click()
    
    #button = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div[1]/form/div[3]/div/div[1]/div[1]/div/span[1]")
    #button.click()

    
    #<span class="as-purchaseinfo-dudeinfo-suffixlabel">Delivers to <button class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink" data-autom="deliveryDateChecker" data-ase-overlay="dude-overlay" data-ase-click="show">27514</button></span>
    
    #inputElement = driver.find_element_by_id("postalCode")
    #inputElement.send_keys('27514')
    #inputElement.submit()
    
    #button = driver.find_element_by_class_name("rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink")
    #button.click()
    
    #<button class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink" data-autom="deliveryDateChecker" data-ase-overlay="dude-overlay" data-ase-click="show">27514</button>
    
    #button = driver.find_element_by_class_name("as-pruchaseinfo-dudeinfo-label")
    #button = driver.find_element_by_xpath('//div[@class="as-purchaseinfo-dudeinfo-dude2"]//span[@class="as-purchaseinfo-dudeinfo-suffixlabel"]//button[@class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink"]')
    #button.click()
    #//span[@class="as-purhcaseinfo-dudeinfo-label"]
    
    #wait = WebDriverWait(driver, 10000)
    #age = wait.until(EC.visibility_of_element_located(button))
    #age.click()
    
    #button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="as-purchaseinfo-dudeinfo-dude2"]//span[@class="as-purchaseinfo-dudeinfo-suffixlabel"]//button[@class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink"]')))
    #button.click()
    
    button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink"]')))
    button.submit()
    
   # <button type="button" class="rf-pickup-quote-overlay-trigger as-retailavailabilitytrigger-infobutton retail-availability-search-trigger as-buttonlink" data-ase-overlay="buac-overlay" data-ase-click="show">Apple Crabtree Valley Mall</button>
    #<button class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink" data-autom="deliveryDateChecker" data-ase-overlay="dude-overlay" data-ase-click="show">27601†† </button>
    time.sleep(5)
    inputElement = driver.find_element_by_id("postalCode")
    inputElement.send_keys('27514')
    inputElement.submit()
    
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'lxml')

    results = soup.find(id="actiontray")

    #print(results.prettify())

    stock_elements = results.find("span", class_="as-retailavailabilitytrigger-value")
    #print(stock_elements)
    #print(stock_elements.text)
    searched = stock_elements.text.split()
    apple_store = searched[searched.index("Apple") + 1]
    print(apple_store)
        
    if "Today" in stock_elements.text:
        return True
    else:
        return False
    


url1 = "https://www.apple.com/shop/buy-mac/macbook-pro/14-inch-space-gray-8-core-cpu-14-core-gpu-512gb#"

check_available(url1)

