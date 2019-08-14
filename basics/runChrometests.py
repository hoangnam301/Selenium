from selenium import webdriver
import os
class RunChrometest():
    def testmethod(self):
        driver=webdriver.Chrome()
        driver.get("https://www.24h.com.vn/")
chrome=RunChrometest()
chrome.testmethod()