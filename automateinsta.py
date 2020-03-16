# Ram Bhattarai
# Automate Instagram Login


# Import important libraries
from selenium import webdriver
from time import sleep
import json
class AutomateInstagram:

    def __init__(self):
        with open("token.json") as reader:
            tokens = json.load(reader)
        self.passwd = tokens["password"]
        self.username = tokens["name"]
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.passwd)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)

AutomateInstagram()
