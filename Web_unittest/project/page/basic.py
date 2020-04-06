from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


from project.toolUtils.logUtils import log
from project.toolUtils.yamlUtils import Yaml
import time

logfile = Yaml("./config/configFile.yaml").readYaml()["logFiles"]["loginLog"].format(time.strftime("%Y-%m-%d"))
logger = log(logfile)

class Page(object):

    def __init__(self, seleniumDriver, baseUrl):
        self.driver = seleniumDriver
        self.baseUrl = baseUrl

    def _open(self, uri):
        url = self.baseUrl + uri
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def open(self, uri):
        self._open(uri)

    def onPage(self, uri):
        return self.driver.current_url == (self.baseUrl + uri)

    def findElement(self, type, eleLoc):
        ele = None
        try:
            if type == "id":
                ele = self.driver.find_element(By.ID, eleLoc)
            elif type == "class_name":
                ele = self.driver.find_element(By.CLASS_NAME, eleLoc)
            elif type == "xpath":
                ele = self.driver.find_element(By.XPATH, eleLoc)
            elif type == "name":
                ele = self.driver.find_element(By.NAME, eleLoc)
            elif type == "css_selector":
                ele = self.driver.find_element(By.CSS_SELECTOR, eleLoc)
            elif type == "link_text":
                ele = self.driver.find_element(By.LINK_TEXT, eleLoc)
            elif type == "partial_link_text":
                ele = self.driver.find_element(By.PARTIAL_LINK_TEXT, eleLoc)
            else:
                ele = self.driver.find_element(By.TAG_NAME, eleLoc)
        except Exception:
            ele = None
            logger.msg("Element: %s NOT Found!!!" % eleLoc, "error")
        else:
            logger.msg("Element: %s Found!" % eleLoc, "info")
        finally:
            return ele

    def getText(self, type, eleLoc):
        return self.findElement(type, eleLoc).text

    def click(self, type, eleLoc):
        self.findElement(type, eleLoc).click()

    def input(self, type, eleLoc, value):
        self.findElement(type, eleLoc).send_keys(value)

    def moveToElement(self, type, eleLoc):
        ele = self.findElement(type, eleLoc)
        ActionChains(self.driver).move_to_element(ele).perform()

    def switch2Frame(self, type, eleLoc):
        ele = self.findElement(type, eleLoc)
        self.driver.switch_to.frame(ele)

    def switch2Default(self):
        self.driver.switch_to.default_content()

    def script(self, src):
        return self.driver.execute_script(src)

    # def sendKeys(self, loc, value, clearFirst=True, clickFirst=True):
    #     try:
    #         loc = getattr(self, '_%s' % loc)
    #         if clickFirst:
    #             self.findElement(*loc).click()
    #         if clearFirst:
    #             self.findElement(*loc).clear()
    #         self.findElement(*loc).send_keys(value)
    #     except AttributeError:
    #         logger.msg("%s page does not have '%s' locator" %(self, loc), "error")

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    douban = Page(driver, "http://www.douban.com/")

    text = douban.getText("class_name","account-tab-account")
    print(text)