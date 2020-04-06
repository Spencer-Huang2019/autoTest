from pytest_bdd import given, when, then, scenario
from toolUtils.elementLoc import eleLoc
import json

@scenario("../../features/doubanlogin.feature", "loginSmsInc")
def test_loginSmsInc():
    pass

@given("Redirect to home page")
def getHome(driver, getData):
    url = getData["baseUrl"] + getData["uri"]
    driver.get(url)

@when('input "<phone>"')
def inputPhone(driver, getData, phone):
    iframeLoc = getData["iframeLoc"]
    frame = eleLoc(driver, iframeLoc["type"], iframeLoc["value"])
    driver.switch_to.frame(frame)

    phoneLoc = getData["phoneLoc"]
    eleLoc(driver, phoneLoc["type"], phoneLoc["value"]).send_keys(phone)

@then('input "<smsCode>"')
def inputSms(driver, getData, smsCode):
    smsLoc = getData["smsCodeLoc"]
    eleLoc(driver, smsLoc["type"],smsLoc["value"]).send_keys(smsCode)

@then("click Login button")
def clickLogin(driver, getData):
    btnLoc = getData["submitLoc"]
    eleLoc(driver, btnLoc["type"], btnLoc["value"]).click()

@then('"<expected>" can be found')
def assertion(driver, expected):
    expectedData = json.loads(expected)
    ele = eleLoc(driver, expectedData["type"], expectedData["value"])
    assert (ele.text == expectedData["text"])