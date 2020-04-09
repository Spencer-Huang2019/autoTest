
class Page(object):

    def __init__(self, seleniumDriver, baseUrl):
        self.driver = seleniumDriver
        self.baseUrl = baseUrl

    def _open(self, uri):
        url = self.baseUrl + uri
        self.driver.get(url)
        self.driver.implicitly_wait(20)

    def open(self, uri):
        self._open(uri)

    def onPage(self, uri):
        return self.driver.current_url == (self.baseUrl + uri)

    def findElement(self, eleLoc):
        try:
            ele = self.driver.find_element(*eleLoc)
        except Exception:
            ele = None
        return ele

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
    pass