from .basic import Page
from selenium.webdriver.common.by import By

class Login(Page):


    def open(self, uri):
        self._open(uri)

    def switchIframe(self, eleLoc):
        print(eleLoc)
        frame = self.findElement(eleLoc)
        self.driver.switch_to.frame(frame)

    def click(self, eleLoc):
        self.findElement(eleLoc).click()

    def typeUser(self, eleLoc, username):
        self.findElement(eleLoc).send_keys(username)

    def typePw(self, eleLoc, password):
        self.findElement(eleLoc).send_keys(password)

    def typePhone(self, eleLoc, phone):
        self.findElement(eleLoc).send_keys(phone)

    def typeSms(self, eleLoc, smsCode):
        self.findElement(eleLoc).send_keys(smsCode)
