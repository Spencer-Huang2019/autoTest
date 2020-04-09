import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../")))

from selenium import webdriver
import pytest
from toolUtils.yamlUtils import Yaml
from toolUtils.openConf import Conf


@pytest.fixture()
def conf():
    return Conf().read()


@pytest.fixture()
def eleLoc(conf):
    elefile = conf["eleFiles"]["loginEle"]
    data = Yaml(elefile).readYaml()
    uri = data["uri"]
    del data["uri"]

    for key,value in data.items():
        data[key] = (value["by"], value["value"])

    return uri, data


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()