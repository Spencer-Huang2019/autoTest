import unittest
from project.toolUtils.yamlUtils import Yaml
from project.page.loginPage import LoginPage
from project.toolUtils.getData import GetData
from parameterized import parameterized
import warnings
from selenium import webdriver
from time import sleep
from project.toolUtils.logUtils import log
import time

logfile = Yaml("./config/configFile.yaml").readYaml()["logFiles"]["loginLog"].format(time.strftime("%Y-%m-%d"))
logger = log(logfile)

configFile = Yaml("./config/configFile.yaml").readYaml()
tcPath = configFile["caseFiles"]["loginTC"]
getObj = GetData(tcPath)

baseUrl = configFile["baseUrl"]
elementDict = Yaml("./config/elementLoc/loginEle.yaml").readYaml()

class TestLogin(unittest.TestCase):

    global baseUrl
    global elementDict

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.baseUrl = baseUrl
        warnings.simplefilter("ignore", ResourceWarning)

    @parameterized.expand(getObj.data())
    def testLogin(self,id, desc, dataDict, expected):
        driver = self.driver
        case = LoginPage(driver, self.baseUrl, elementDict, id, desc, dataDict)
        logger.msg("case: %s START!" %desc, "info")
        if id == "1":
            case.pwLoginSucess()
            assert (case.findElement(expected["type"], expected["value"]) != None)
        elif id == "2":
            case.loginPhInc()
            # assert if error pops
            assert (case.findElement(expected["type"], expected["value"]) != None)
            assert (case.getText(expected["type"], expected["value"]) == expected["text"])
        elif id == "3":
            case.loginSmsInc()
            # assert if error pops
            assert (case.findElement(expected["type"], expected["value"]) != None)
            assert (case.getText(expected["type"], expected["value"]) == expected["text"])
        elif id == "4":
            case.loginPwInc()
            # assert if error pops
            assert (case.findElement(expected["type"], expected["value"]) != None)
            assert (case.getText(expected["type"], expected["value"]) == expected["text"])
        else:
            case.logout()
            # assert if logout success
            assert (case.findElement(expected["type"], expected["value"]) != None)
        logger.msg("case: %s FINISHED!" % desc, "info")
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
    # filepath = "../config/loginEle.yaml"

    unittest.main()
