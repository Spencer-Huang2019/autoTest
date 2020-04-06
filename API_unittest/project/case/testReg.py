from project.toolUtils.getData import getData
from project.api.baseApi import BusApi
import unittest
from parameterized import parameterized
from project.toolUtils.yamlUtils import Yaml
import time

class testRegister(unittest.TestCase):

    tcFilepath = Yaml("./config/config.yaml").readYaml()["caseFile"]["path"].format(time.strftime("%Y-%m-%d"))
    sheetName = Yaml("./config/config.yaml").readYaml()["caseFile"]["registerSheet"].format(time.strftime("%Y-%m-%d"))
    getObj = getData(tcFilepath, sheetName)

    @parameterized.expand(getObj.data())
    def test(self, id, desc, url, method, headers, payload, expected):
        res = BusApi(id, desc, url, method, headers, payload, expected, "register")
        res.assertion()