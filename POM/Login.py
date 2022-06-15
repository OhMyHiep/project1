from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Login:

    def __init__(self, driver:WebDriver):
        self.driver=driver

    def getLoginPage(self):
        return self.driver.get('http://127.0.0.1:5000/login')

    def username(self):
        return self.driver.find_element(By.ID,"username")

    def password(self):
        return self.driver.find_element(By.ID,"password1")

    def submit(self):
        return self.driver.find_element(By.ID,"submit")

    def loginUser(self,username,password):
        self.getLoginPage()
        self.username().send_keys(username)
        self.password().send_keys(password)
        self.submit().click()
