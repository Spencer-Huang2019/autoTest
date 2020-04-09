import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../")))

from page.pageLogin import Login
import pytest
import allure
from toolUtils.getData import GetData
from toolUtils.openConf import Conf

dataF = Conf().read()["caseFiles"]["phInc"]
caseData = GetData(dataF).data()

@allure.feature("Login module testing")
@allure.story("Login with incorrect phone number")
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
    allure.attach("phone:{}".format(input["phone"]), "Input data")

    loginPage.click(eleDict["sendSMSLoc"])

    expected = testData[1]
    allure.attach("Expected:Should find the element {}".format(expected), "Expected assertion")
    expectedEle = loginPage.findElement((expected["by"], expected["value"]))
    assert (expectedEle is not None)
    assert (expectedEle.text == "请正确填写手机号")