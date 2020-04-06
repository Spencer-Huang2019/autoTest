from .basic import Page
from selenium.webdriver.common.action_chains import ActionChains

class BaiduPage(Page):

    def open(self, url):
        self._open(url)

    def typeInput(self, searchLoc, searchValue):
        self.findElement(*searchLoc).send_keys(searchValue)

    def click(self, args):
        self.findElement(*args).click()

    def moveToElement(self, eleLoc):
        ele = self.findElement(*eleLoc)
        ActionChains(self.driver).move_to_element(ele).perform()

    def switch2Frame(self, iframLoc):
        ele = self.findElement(*iframLoc)
        self.driver.switch_to.frame(ele)

    def switch2Default(self):
        self.driver.swith_to.default_content()