from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .Login import Login

class NavBar:

    def __init__(self,driver:WebDriver):
        self.driver=driver
        self.login=Login(driver)

    def getBtnById(self,button):
        return self.driver.find_element(By.ID,button)





