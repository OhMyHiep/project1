from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ReimbursementPage:

    def __init__(self, driver:WebDriver):
        self.driver=driver

    def getReimbursementPage(self):
        return self.driver.get('http://127.0.0.1:5000/reimbursement-page')

    def getTitle(self):
        return self.driver.title

    def selectCategory(self):
        return self.driver.find_element(By.ID,"inputGroupSelect01")

    def description(self):
        return self.driver.find_element(By.XPATH,'"//*[@id="request"]/input[1]"')