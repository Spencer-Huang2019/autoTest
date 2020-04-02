from project.toolUtils import excelUtils
from project.toolUtils.logUtils import log
from project.toolUtils.getData import getData
from project.api.login import loginApi
import unittest
from parameterized import parameterized
import json

logfile = "./logFile/loginApi_log.txt"
filepath = "./data/api_TC_result.xls"
sheetName = "login"
getObj = getData(filepath, sheetName)

logger = log(logfile)

class testLogin(unittest.TestCase):

    @parameterized.expand(getObj.data())
    def test(self, id, desc, url, method, headers, payload, expected):
        row = int(id)
        logger.msg("TC%d %s: [url:%s headers:%s payload:%s expected:%s]" % (row,desc,url,headers,payload,expected),"info")
        # logger.msg("payload type: %s" % type(payload), "info")
        # logger.msg("headers type: %s" % type(headers), "info")

        http = loginApi(url,method,headers,payload)
        res = http.request()
        statusCode = res.status_code
        logger.msg("TC%d %s: [statusCode:%d]" % (row, desc, statusCode),"info")

        # write result into excel
        global filepath
        global sheetName
        workBook = excelUtils.excelRead(filepath).open()
        wr = excelUtils.excelWrite(filepath, workBook)

        expected_payload = json.loads(expected)
        testResult = ""
        if statusCode == 200:
            res_payload = res.json()
            logger.msg("TC%d %s: [response:%s, expected:%s]" % (row,desc,res_payload,expected), "info")
            wr.write(sheetName,row,7,json.dumps(res_payload))

            try:
                assert (res_payload["msg"] == expected_payload["msg"])
                assert (res_payload["status"] == expected_payload["status"])
                assert (res_payload["errorCode"] == expected_payload["errorCode"])
            except Exception:
                testResult = "FAIL"
            else:
                testResult = "PASS"
            finally:
                wr.write(sheetName, row, 8, testResult)

        else:
            wr.write(sheetName, row, 7, res.status_code)
            testResult = "FAIL"
            wr.write(sheetName, row, 8, testResult)
        logger.msg("TC%d %s: [testResult:%s]" % (row, desc, testResult), "info")