import unittest
from project.page.baiduSearch import BaiduPage
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# class TestLogin(unittest.TestCase):

def testBaidu(uri, driver, searchLoc,submitLoc, searchValue):

    baiduPage = BaiduPage(driver)
    baiduPage.open(uri)
    baiduPage.typeInput(searchLoc, searchValue)
    baiduPage.click(submitLoc)
    sleep(3)

if __name__ == '__main__':

    uri = "/"
    searchLoc = (By.ID, "kw")
    submitLoc = (By.ID, "su")

    driver = webdriver.Chrome()
    searchValue = "python3"
    testBaidu(uri, driver, searchLoc, submitLoc, searchValue)
