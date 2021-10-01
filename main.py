from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

INSTAGRAM_URL = 'https://www.instagram.com'
DRIVER_PATH = 'chromedriver/chromedriver.exe'
# i've installed Chrome version 94. Please download chromedriver for your chrome version

# to disable logs please uncomment code below

#options = webdriver.ChromeOptions()
#options.add_argument('--log-level=OFF')
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
#chrome_driver = webdriver.Chrome(executable_path="chromedriver/chromedriver.exe", options=options)


chrome_driver = webdriver.Chrome(executable_path=DRIVER_PATH)

class Bot:
    def __init__(self,username,psw,targetId,comment):
        self.driver = chrome_driver
        self.driver.maximize_window()
        self.driver.get(INSTAGRAM_URL)
        sleep(3) # this will keep chrome opened
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username) # get username input
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(psw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(5)

        # now, 3 pop up appears... have to say no :)
        self.driver.find_element_by_xpath("//button[text()='Ahora no']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[text()='Ahora no']").click()
        sleep(3)
        self.driver.get(INSTAGRAM_URL+"/{}".format(targetId))
        print()
        sleep(3)

print("\n"*3)
print("-"*50+"\n")
print("-"*50+"\n")
print("-"*13+"Welcome to instagram bot!"+"-"*13+"\n")
print("-"*50+"\n")
print("-"*50+"\n")
print("\n"*3)
your_username = input("Please type your username: ")
print("\n"*2)
password = input("Please type your password: ")


Bot(your_username,password,'target','hi')