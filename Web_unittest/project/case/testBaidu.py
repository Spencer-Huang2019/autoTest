import unittest
# from project.page.baiduSearch import BaiduPage
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
#
# # class TestLogin(unittest.TestCase):
#
# def testBaidu(uri, driver, searchLoc,submitLoc, searchValue):
#
#     baiduPage = BaiduPage(driver)
#     baiduPage.open(uri)
#     baiduPage.typeInput(searchLoc, searchValue)
#     baiduPage.click(submitLoc)
#     sleep(3)
#
if __name__ == '__main__':


    driver = webdriver.Chrome()
    driver.get("http://www.douban.com/")
    driver.implicitly_wait(10)

    frame = driver.find_element_by_css_selector(".login>iframe")
    driver.switch_to.frame(frame)

    driver.find_element_by_class_name("account-tab-account").click()

    driver.find_element_by_id("username").send_keys("15122888806")

    driver.find_element_by_id("password").send_keys("huanhuan350881")

    driver.find_element_by_link_text("登录豆瓣").click()

    windows = driver.window_handles
    print(windows)
    driver.find_element_by_xpath("//*[@id='db-global-nav']/div/div[1]/ul/li[2]/a").click()

    driver.find_element_by_link_text("退出").click()

    # assert if logout success
    assert (driver.find_element_by_link_text("登录豆瓣") != None)
