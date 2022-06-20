from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ReimbursementPage:

    def __init__(self, driver:WebDriver):
        self.driver=driver

    def getReimbursementPage(self):
        return self.driver.get('http://127.0.0.1:5000/reimbursement-page')

    def getTitle(self):
        return self.driver.title

    def selectCategory(self,type):
        dropDown = self.driver.find_element(By.XPATH,"//*[@id='inputGroupSelect01']")
        dropDownMenu = Select(dropDown)
        return dropDownMenu.select_by_visible_text(type)
        

    def description(self):
        return self.driver.find_element(By.XPATH,"//*[@id='request']/*[@type='text']")

    def amount(self):
        return self.driver.find_element(By.XPATH,"//*[@id='request']/*[@type='number']")

    def submitBtn(self):
        return self.driver.find_element(By.XPATH,'//*[@id="request"]/span/input')

    def getCurrentPageTitle(self):
        return self.driver.title