from .basic import Page
from project.toolUtils.logUtils import log
from project.toolUtils.yamlUtils import Yaml
import time

logfile = Yaml("./config/configFile.yaml").readYaml()["logFiles"]["loginLog"].format(time.strftime("%Y-%m-%d"))
logger = log(logfile)

class LoginPage(Page):

    def __init__(self, driver, baseUrl, eleDict, id,  desc, dataDict):
        super().__init__(driver, baseUrl)
        self.eleDict = eleDict
        self.id = id
        self.desc = desc
        self.dataDict = dataDict
        self.open(self.eleDict["uri"]["value"])

    def pwLoginSucess(self):

        # switch to iframe
        eleIframe = self.eleDict["iframeLoc"]
        self.switch2Frame(eleIframe["type"], eleIframe["value"])

        # select way of login, phone&pw
        eleWayOf = self.eleDict["pwWayOfLoc"]
        self.click(eleWayOf["type"], eleWayOf["value"])

        eleUser = self.eleDict["usernameLoc"]
        self.input(eleUser["type"], eleUser["value"], self.dataDict["username"])
        logger.msg("Enter username: %s" % self.dataDict["username"], "info")

        elePw = self.eleDict["passwordLoc"]
        self.input(elePw["type"], elePw["value"], self.dataDict["password"])
        logger.msg("Enter password: %s" % self.dataDict["password"], "info")

        # submit to login
        eleClick = self.eleDict["submitLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("User clicked login!", "info")

        self.switch2Default()

    def loginPhInc(self):

        # switch to iframe
        eleIframe = self.eleDict["iframeLoc"]
        self.switch2Frame(eleIframe["type"], eleIframe["value"])
        # default way of login is phone

        elePhone = self.eleDict["phoneLoc"]
        self.input(elePhone["type"], elePhone["value"], self.dataDict["phone"])
        logger.msg("Enter phone: %s" % self.dataDict["phone"], "info")

        # click to send SMScode
        eleClick = self.eleDict["sendSMSLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Click send SMS", "info")

    def loginSmsInc(self):

        # switch to iframe
        eleIframe = self.eleDict["iframeLoc"]
        self.switch2Frame(eleIframe["type"], eleIframe["value"])
        # default way of login is phone

        elePhone = self.eleDict["phoneLoc"]
        self.input(elePhone["type"], elePhone["value"], self.dataDict["phone"])
        logger.msg("Enter phone: %s" % self.dataDict["phone"], "info")

        eleSms = self.eleDict["smsCodeLoc"]
        self.input(eleSms["type"], eleSms["value"], self.dataDict["smsCode"])
        logger.msg("Enter smsCode: %s" % self.dataDict["smsCode"], "info")

        # click to login
        eleClick = self.eleDict["submitLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Click to login", "info")

    def loginPwInc(self):

        # switch to iframe
        eleIframe = self.eleDict["iframeLoc"]
        self.switch2Frame(eleIframe["type"], eleIframe["value"])
        # select way of login, phone&pw
        eleWayOf = self.eleDict["pwWayOfLoc"]
        self.click(eleWayOf["type"], eleWayOf["value"])

        eleUser = self.eleDict["usernameLoc"]
        self.input(eleUser["type"], eleUser["value"], self.dataDict["username"])
        logger.msg("Enter username: %s" % self.dataDict["username"], "info")
        elePw = self.eleDict["passwordLoc"]
        self.input(elePw["type"], elePw["value"], self.dataDict["password"])
        logger.msg("Enter password: %s" % self.dataDict["password"], "info")

        # click to login
        eleClick = self.eleDict["submitLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Click to login", "info")


    def logout(self):

        self.pwLoginSucess()

        # click userAcc
        eleClick = self.eleDict["myAccLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Show item of myAccount", "info")

        # click logout
        eleClick = self.eleDict["logoutLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Logout DouBan", "info")

        # switch to iframe
        eleIframe = self.eleDict["iframeLoc"]
        self.switch2Frame(eleIframe["type"], eleIframe["value"])