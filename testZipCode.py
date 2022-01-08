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
    driver = webdriver.Firefox()
    
    driver.get(url_check)
    #Click to change zipcode
    #wait = WebDriverWait(driver, 10)
    #button = driver.find_element_by_class_name("rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink")
    #button.click()
    
    wait = WebDriverWait(driver, 100)
    age = wait.until(EC.visibility_of_element_located((driver.find_element_by_class_name("as-purchaseinfo-dudeinfo-label"))))
    age.click()
    
    #button = driver.find_element_by_class_name("as-purchaseinfo-dudeinfo-label")
    #button.click()
    
    #button = driver.find_element(By.CSS_SELECTOR("#actiontray > div > div.toggletray > div.as-actiontray-deliverydates > div > span.as-purchaseinfo-dudeinfo-suffixlabel > button"))
    #button.click()
    
    #button = driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/div[1]/form/div[3]/div/div[1]/div[1]/div/span[1]")
    #button.click()

    
    #<span class="as-purchaseinfo-dudeinfo-suffixlabel">Delivers to <button class="rf-dude-quote-overlay-trigger as-delivery-overlay-trigger as-purchaseinfo-dudetrigger as-buttonlink" data-autom="deliveryDateChecker" data-ase-overlay="dude-overlay" data-ase-click="show">27514</button></span>
    
    inputElement = driver.find_element_by_id("postalCode")
    inputElement.send_keys('27514')
    inputElement.submit()
    time.sleep(1)
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
url2 = "https://www.apple.com/shop/buy-mac/macbook-pro/13-inch-space-gray-apple-m1-chip-with-8-core-cpu-and-8-core-gpu-256gb#"
url3 = "https://www.apple.com/shop/buy-mac/macbook-pro/13-inch-space-gray-apple-m1-chip-with-8-core-cpu-and-8-core-gpu-512gb#"
url4 = "https://www.apple.com/shop/buy-mac/macbook-pro/13-inch-silver-apple-m1-chip-with-8-core-cpu-and-8-core-gpu-256gb#"


model_name = [""]*4
in_stock = [False]*4

def fill_stock(urls_check):
    n = len(urls_check)
    for x in range(n):
        in_stock[x] = check_available(urls_check[x])

model_urls = [url1,url2,url3,url4]

fill_stock(model_urls)
print(in_stock)

