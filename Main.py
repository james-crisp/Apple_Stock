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

#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options)

#apple_store = ''

def check_available(url_check):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    
    driver.get(url_check)
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
