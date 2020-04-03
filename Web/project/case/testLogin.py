import unittest
from project.toolUtils.yamlUtils import Yaml
from project.page.loginPage import LoginPage
from project.toolUtils.getData import GetData
from project.toolUtils.logUtils import log
from parameterized import parameterized
import warnings
from selenium import webdriver
from time import sleep

logfile = "./logFiles/testLogin_log.txt"
logger = log(logfile)

filepath = "./data/loginTC.json"
getObj = GetData(filepath)

configDict = Yaml(getObj.configFile()).readYaml()

class TestLogin(unittest.TestCase):

    global configDict
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.baseUrl = configDict["baseUrl"]["value"]
        warnings.simplefilter("ignore", ResourceWarning)

    @parameterized.expand(getObj.testData())
    def testLogin(self,id, desc, dataDict, expected):
        driver = self.driver
        case = LoginPage(driver, self.baseUrl, configDict, id, desc, dataDict, expected)
        if id == "1":
            case.pwLoginSucess()
        elif id == "2":
            case.loginPhInc()
        elif id == "3":
            case.loginSmsInc()
        elif id == "4":
            case.loginPwInc()
        else:
            case.logout()
        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    # testData = {
    #     "uri":"/",
    #     "iframeLoc":(By.XPATH, "//div[@class='login']/iframe"),
    #     "wayOfLoc":(By.CLASS_NAME, "account-tab-account"),
    #     "usernameLoc":(By.ID, "username"),
    #     "passwordLoc":(By.ID, "password"),
    #     "username": "15122888806",
    #     "password": "huanhuan350881",
    #     "submitLoc":(By.LINK_TEXT, "登录豆瓣")
    # }
    # inData = {"username": "15122888806","password": "huanhuan350881"}
    # filepath = "../config/loginConfig.yaml"

    unittest.main()

    driver = webdriver.Chrome()
    driver.get("http://www.douban.com/")
    driver.implicitly_wait(10)
    ele = driver.find_element_by_class_name("ss")

    # frame = driver.find_element_by_css_selector(".login>iframe")
    # driver.switch_to.frame(frame)
    # print(frame)
    # ele = driver.find_element_by_class_name("account-tab-account on")
    # print(ele)