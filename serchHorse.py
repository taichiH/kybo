# -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver

def serch():
    search_word = unicode("ロックディスタウン", "utf-8")
    browser = webdriver.Chrome('./chromedriver')
    browser.get('http://db.netkeiba.com/?pid=horse_top')
    time.sleep(1)
    search_input = browser.find_element_by_css_selector(".field")
    search_input.send_keys(search_word)
    search_input.submit()
    time.sleep(1)
    
    return browser.current_url
