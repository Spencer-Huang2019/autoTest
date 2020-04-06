from pytest_bdd import given, when, then, scenario
from toolUtils.elementLoc import eleLoc
import json

@scenario("../../features/doubanlogin.feature", "loginPwInc")
def test_loginPwInc():
    pass

@given("Redirect to home page")
def getHome(driver, getData):
    url = getData["baseUrl"] + getData["uri"]
    driver.get(url)

@when("Select the PW way of loggin")
def select(driver, getData):
    iframeLoc = getData["iframeLoc"]
    frame = eleLoc(driver, iframeLoc["type"], iframeLoc["value"])
    driver.switch_to.frame(frame)

    pwWay = getData["pwWayOfLoc"]
    eleLoc(driver, pwWay["type"], pwWay["value"]).click()

@then('input "<username>" and incorrect "<password>"')
def input(driver, getData, username, password):
    usernameLoc = getData["usernameLoc"]
    passwordLoc = getData["passwordLoc"]
    eleLoc(driver, usernameLoc["type"], usernameLoc["value"]).send_keys(username)
    eleLoc(driver, passwordLoc["type"], passwordLoc["value"]).send_keys(password)

@then("click Login button")
def clickLogin(driver, getData):
    btnLoc = getData["submitLoc"]
    eleLoc(driver, btnLoc["type"], btnLoc["value"]).click()

@then('"<expected>" can be found')
def assertion(driver, expected):
    expectedData = json.loads(expected)
    ele = eleLoc(driver, expectedData["type"], expectedData["value"])
    assert (ele.text == expectedData["text"])