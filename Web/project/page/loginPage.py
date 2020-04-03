from .basic import Page
from project.toolUtils.logUtils import log

logfile = "./logFiles/testLogin_log.txt"
logger = log(logfile)

class LoginPage(Page):

    def __init__(self, driver, baseUrl, configDict, id,  desc, dataDict, expected):
        super().__init__(driver, baseUrl)
        self.configDict = configDict
        self.id = id
        self.desc = desc
        self.dataDict = dataDict
        self.expected = expected
        self.open(self.configDict["uri"]["value"])
        logger.msg("Open the url: {}{}".format(self.configDict["baseUrl"], self.configDict["uri"]), "info")

    def pwLoginSucess(self):

        # switch to iframe
        eleIframe = self.configDict["iframeLoc"]
        self.switch2Frame(eleIframe["type"], eleIframe["value"])
        # select way of login, phone&pw
        eleWayOf = self.configDict["pwWayOfLoc"]
        self.click(eleWayOf["type"], eleWayOf["value"])
        eleUser = self.configDict["usernameLoc"]
        self.input(eleUser["type"], eleUser["value"], self.dataDict["username"])
        logger.msg("Enter username: %s" % self.dataDict["username"], "info")
        elePw = self.configDict["passwordLoc"]
        self.input(elePw["type"], elePw["value"], self.dataDict["password"])
        logger.msg("Enter password: %s" % self.dataDict["password"], "info")

        # submit to login
        eleClick = self.configDict["submitLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("User successfully login!", "info")

        self.switch2Default()

        # assert if login success
        if self.expected:
            try:
                assert (self.findElement(self.expected["type"], self.expected["value"]) != None)
            except Exception:
                logger.msg("Case{}: {} FAIL!!!".format(self.id, self.desc), "error")
            else:
                logger.msg("Case{}: {} PASS!".format(self.id, self.desc), "info")

    def loginPhInc(self):

        # switch to iframe
        eleIframe = self.configDict["iframeLoc"]
        self.switch2Frame(eleIframe["type"], eleIframe["value"])
        # default way of login is phone

        elePhone = self.configDict["phoneLoc"]
        self.input(elePhone["type"], elePhone["value"], self.dataDict["phone"])
        logger.msg("Enter phone: %s" % self.dataDict["phone"], "info")

        # click to send SMScode
        eleClick = self.configDict["sendSMSLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Click send SMS", "info")

        # assert if error pops
        if self.expected:
            try:
                assert (self.findElement(self.expected["type"], self.expected["value"]) != None)
                assert (self.getText(self.expected["type"], self.expected["value"]) == self.expected["text"])
            except Exception:
                logger.msg("Case{}: {} FAIL!!!".format(self.id, self.desc), "error")
            else:
                logger.msg("Case{}: {} PASS!".format(self.id, self.desc), "info")

    def loginSmsInc(self):

        # switch to iframe
        eleIframe = self.configDict["iframeLoc"]
        self.switch2Frame(eleIframe["type"], eleIframe["value"])
        # default way of login is phone

        elePhone = self.configDict["phoneLoc"]
        self.input(elePhone["type"], elePhone["value"], self.dataDict["phone"])
        logger.msg("Enter phone: %s" % self.dataDict["phone"], "info")

        eleSms = self.configDict["smsCodeLoc"]
        self.input(eleSms["type"], eleSms["value"], self.dataDict["smsCode"])
        logger.msg("Enter smsCode: %s" % self.dataDict["smsCode"], "info")

        # click to login
        eleClick = self.configDict["submitLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Click to login", "info")

        # assert if error pops
        if self.expected:
            try:
                assert (self.findElement(self.expected["type"], self.expected["value"]) != None)
                assert (self.getText(self.expected["type"], self.expected["value"]) == self.expected["text"])
            except Exception:
                logger.msg("Case{}: {} FAIL!!!".format(self.id, self.desc), "error")
            else:
                logger.msg("Case{}: {} PASS!".format(self.id, self.desc), "info")

    def loginPwInc(self):

        # switch to iframe
        eleIframe = self.configDict["iframeLoc"]
        self.switch2Frame(eleIframe["type"], eleIframe["value"])
        # select way of login, phone&pw
        eleWayOf = self.configDict["pwWayOfLoc"]
        self.click(eleWayOf["type"], eleWayOf["value"])

        eleUser = self.configDict["usernameLoc"]
        self.input(eleUser["type"], eleUser["value"], self.dataDict["username"])
        logger.msg("Enter username: %s" % self.dataDict["username"], "info")
        elePw = self.configDict["passwordLoc"]
        self.input(elePw["type"], elePw["value"], self.dataDict["password"])
        logger.msg("Enter password: %s" % self.dataDict["password"], "info")

        # click to login
        eleClick = self.configDict["submitLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Click to login", "info")

        # assert if error pops
        if self.expected:
            try:
                assert (self.findElement(self.expected["type"], self.expected["value"]) != None)
                assert (self.getText(self.expected["type"], self.expected["value"]) == self.expected["text"])
            except Exception:
                logger.msg("Case{}: {} FAIL!!!".format(self.id, self.desc), "error")
            else:
                logger.msg("Case{}: {} PASS!".format(self.id, self.desc), "info")

    def logout(self):
        self.pwLoginSucess()
        # click userAcc
        eleClick = self.configDict["myAccLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Show item of myAccount", "info")

        # click logout
        eleClick = self.configDict["logoutLoc"]
        self.click(eleClick["type"], eleClick["value"])
        logger.msg("Logout DouBan", "info")

        # assert if logout success
        if self.expected:
            try:
                assert (self.findElement(self.expected["type"], self.expected["value"]) != None)
            except Exception:
                logger.msg("Case{}: {} FAIL!!!".format(self.id, self.desc), "error")
            else:
                logger.msg("Case{}: {} PASS!".format(self.id, self.desc), "info")
