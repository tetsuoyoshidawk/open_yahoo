# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Firefox()

url = r'https://www.yahoo.co.jp/'

driver.get(url)
