from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

class HomePage:

    def __init__(self, driver:WebDriver):
        self.driver=driver

    def getHomePage(self):
        return self.driver.get('http://127.0.0.1:5000')

    def getTitle(self):
        return self.driver.title

    def AddRequestBtn(self):
        return self.driver.find_element(By.ID,"AddRequest")

    def ViewAllBtn(self):
        return self.driver.find_element(By.ID,"ViewAllBtn")

    def DeleteRequestBtn(self):
        return self.driver.find_element(By.ID,"DeleteRequest")

    def ViewAllContainer(self):
        return self.driver.find_element(By.XPATH,"//*[@id=\"viewAllRequests\"]/table")

    def DeleteContainer(self):
        return self.driver.find_element(By.XPATH,"//*[@id=\"viewAllRequests\"]/table")       

    def cancelBtn(self):
        return self.driver.find_element(By.XPATH,"//*[text()='pending']/following-sibling::*/button[@type='CancelRequest']") 

    def deleteBtn(self,req_id):
        return self.driver.find_element(By.XPATH,f"*//table/tbody/tr/*[text()='{req_id}']/following-sibling::*/button[@type='DeleteRequest']")

    def getPendingRequestId(self):
        return self.driver.find_element(By.XPATH,"//*[text()='pending']//parent::tr/td[1]")

    def findReqStatus(self,req_id):
        #req_id=self.driver.find_element(By.XPATH,"*//table/tbody/tr/td[1]").text
        return self.driver.find_element(By.XPATH,f"*//table/tbody/tr/*[text()='{req_id}']/following-sibling::td[@style='color:red']")

    def findDeletedRecord(self,req_id):
        return self.driver.find_element(By.XPATH,f"*//table/tbody/tr/td[1][text()='{req_id}']")
    
    def refreshPage(self):
        return self.driver.refresh()

    def clickAlertbox(self):
        alert=Alert(self.driver)
        print(f"alert find {alert}")
        alert.accept()
        return 

    def getRequestId(self,type):
        return self.driver.find_element(By.XPATH,f"//*[text()='{type}']//parent::tr/td[1]")
        