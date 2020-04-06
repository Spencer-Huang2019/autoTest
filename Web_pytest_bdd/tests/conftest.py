import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import pytest
from selenium import webdriver
from toolUtils.yamlUtils import Yaml

@pytest.fixture()
def driver():
    d = webdriver.Chrome()
    d.implicitly_wait(15)
    yield d
    d.quit()

configFile = Yaml("./config/configFile.yaml").readYaml()
paramData = Yaml("./config/elementLoc/loginEle.yaml").readYaml()
paramData.update(baseUrl = configFile["baseUrl"])

@pytest.fixture()
def getData():
    return paramData