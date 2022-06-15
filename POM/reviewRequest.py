from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from .Login import Login



class ReviewRequest:

    def __init__(self,driver:WebDriver):#,driver:WebDriver
        # self.driver=webdriver.Chrome("/Users/hiephuynh/Documents/revature/project1/drivers/chromedriver")
        self.driver=driver
        self.driver.implicitly_wait(5)
        self.login=Login(self.driver)
        self.has_requests=None
        self.comments=None
        self.request_id=None

    def getReviewRequestPage(self):
        self.driver.get("http://127.0.0.1:5000/review-request")

    def getComments(self):
        elements =self.driver.find_elements(By.ID,"comments")
        self.has_requests=len(elements)!=0
        self.comments= elements[0] if len(elements)>0 else None
        return self.comments

    def getButton(self,button):
        if self.comments:
            reimbursement=self.comments.find_element(By.XPATH,f"../..")
            self.request_id=reimbursement.get_attribute("id")
            return reimbursement.find_element(By.XPATH,f".//button[@value='{button}']")
            

# if __name__=='__main__':
#     driver=webdriver.Chrome("/Users/hiephuynh/Documents/revature/project1/drivers/chromedriver")
#     r=ReviewRequest(driver)
#     r.login.loginUser('testing','testing')
#     r.getReviewRequestPage()
#     r.getComments().send_keys("testing")
#     r.getButton("Accepted").click()

    
