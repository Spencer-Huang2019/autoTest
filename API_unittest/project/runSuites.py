import unittest
import time
from project.toolUtils.HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./case", pattern="test*.py")

# runner = unittest.TextTestRunner()
# runner.run(suite)

file_path = "./reports/{}.html".format(time.strftime("%Y-%m-%d"))

with open(file_path, "wb") as f:
    HTMLTestRunner(stream=f).run(suite)