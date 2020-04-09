import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../")))

from page.pageLogin import Login
import pytest
import allure
from toolUtils.getData import GetData
from toolUtils.openConf import Conf

dataF = Conf().read()["caseFiles"]["smsInc"]
caseData = GetData(dataF).data()

@allure.feature("Login module testing")
@allure.story("Login with incorrect sms code")
@allure.severity("normal")
@pytest.mark.inc
@pytest.mark.parametrize("testData", caseData)
def test_pwSuc(browser, conf, eleLoc, testData):
    baseUrl = conf["baseUrl"]
    uri, eleDict = eleLoc

    loginPage = Login(browser, baseUrl)
    loginPage.open(uri)
    allure.attach(baseUrl + uri, "Request Url")

    loginPage.switchIframe(eleDict["iframeLoc"])

    input = testData[0]
    loginPage.typeUser(eleDict["phoneLoc"], input["phone"])
    loginPage.typeUser(eleDict["smsCodeLoc"], input["smsCode"])
    allure.attach("phone:{} smsCodeL{}".format(input["phone"], input["smsCode"]), "Input data")

    loginPage.click(eleDict["submitLoc"])

    expected = testData[1]
    allure.attach("Expected:Should find the element {}".format(expected), "Expected assertion")
    expectedEle = loginPage.findElement((expected["by"], expected["value"]))
    assert (expectedEle is not None)
    assert (expectedEle.text == "验证码输入错误或已过期")