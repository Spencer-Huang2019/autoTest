import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../")))

from page.pageLogin import Login
import pytest
import allure
from toolUtils.getData import GetData
from toolUtils.openConf import Conf

dataF = Conf().read()["caseFiles"]["pwSuc"]
caseData = GetData(dataF).data()

@allure.feature("Login module testing")
@allure.story("Login with password successfully")
@allure.severity("blocker")
@pytest.mark.smoke
@pytest.mark.parametrize("testData", caseData)
def test_pwSuc(browser, conf, eleLoc, testData):
    baseUrl = conf["baseUrl"]
    uri, eleDict = eleLoc

    loginPage = Login(browser, baseUrl)
    loginPage.open(uri)
    allure.attach(baseUrl + uri, "Request Url")

    loginPage.switchIframe(eleDict["iframeLoc"])
    loginPage.click(eleDict["pwWayOfLoc"])

    input = testData[0]
    loginPage.typeUser(eleDict["usernameLoc"], input["username"])
    loginPage.typePw(eleDict["passwordLoc"], input["password"])
    allure.attach("username:{}, password:{}".format(input["username"], input["password"]), "Input data")

    loginPage.click(eleDict["submitLoc"])

    loginPage.switch2Default()

    expected = testData[1]
    allure.attach("Expected:Should find the element {}".format(expected), "Expected assertion")
    assert (loginPage.findElement((expected["by"], expected["value"])) is not None)
