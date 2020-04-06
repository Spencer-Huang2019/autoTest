from pytest_bdd import given, when, then, scenario
from toolUtils.logUtils import log
from toolUtils.yamlUtils import Yaml
import time
import json
from toolUtils.elementLoc import eleLoc

logfile = Yaml("./config/configFile.yaml").readYaml()["logFiles"]["loginLog"].format(time.strftime("%Y-%m-%d"))
logger = log(logfile)

@scenario("../../features/doubanlogin.feature", "pwLoginSuccess")
def test_loginSuc():
    pass

@given("Redirect to home page")
def getHome(driver, getData):
    url = getData["baseUrl"] + getData["uri"]
    driver.get(url)
    logger.msg("Redirect to Url: %s" %url, "info")

@when("Select the PW way of loggin")
def select(driver, getData):
    iframeLoc = getData["iframeLoc"]
    frame = eleLoc(driver, iframeLoc["type"], iframeLoc["value"])
    driver.switch_to.frame(frame)

    pwWay = getData["pwWayOfLoc"]
    eleLoc(driver, pwWay["type"], pwWay["value"]).click()
    logger.msg("Using password to login", "info")

@then('input "<username>" and "<password>"')
def input(driver, getData, username, password):
    usernameLoc = getData["usernameLoc"]
    passwordLoc = getData["passwordLoc"]
    eleLoc(driver, usernameLoc["type"],usernameLoc["value"]).send_keys(username)
    eleLoc(driver, passwordLoc["type"],passwordLoc["value"]).send_keys(password)
    logger.msg("input username: %s and password" %username, "info")

@then("click Login button")
def clickLogin(driver, getData):
    btnLoc = getData["submitLoc"]
    eleLoc(driver, btnLoc["type"],btnLoc["value"]).click()
    driver.switch_to.default_content()
    logger.msg("Click login btn", "info")

@then('"<expected>" can be found')
def assertion(driver, expected):
    logger.msg("expected: {}, type:{}".format(expected, type(expected)), "info")
    expectedData = json.loads(expected)
    ele = eleLoc(driver, expectedData["type"],expectedData["value"])
    assert(ele.text == expectedData["text"])
    logger.msg("login success", "info")