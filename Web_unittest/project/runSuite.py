from project.toolUtils.HTMLTestRunner import HTMLTestRunner
import unittest
import time

suite = unittest.defaultTestLoader.discover("./case", pattern="testL*.py")

reportFile = "./reports/{}.html".format(time.strftime("%Y-%m-%d"))

with open(reportFile, "wb") as f:
    HTMLTestRunner(stream=f).run(suite)