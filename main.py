from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from re import subn
from decimal import Decimal

# i've installed Chrome version 94. Please download chromedriver for your chrome version
chrome_driver = webdriver.Chrome("chromedriver.exe")
insta_url = 'https://www.instagram.com'

class Bot:
    def __init__(self,username,psw,targetId,comment):
        self.driver = chrome_driver
        self.driver.maximize_window()
        self.driver.get(insta_url)
        sleep(3) # this will keep chrome opened
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username) # get username input
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(psw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(5)
Bot('test','pswtest','agustingrigaliunas','hi')