

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


class ReviewRequest:

    def __init__(self):
        self.driver=webdriver.Chrome("/Users/hiephuynh/Documents/revature/project1/drivers/chromedriver")

        self.has_requests=False

    def hasRequest(self)->bool:

        try:
            self.driver.get("http://127.0.0.1:5000/review-request")
            elements =self.driver.find_elements(By.ID,"comments")
            print(f'title: {self.driver.title}')
            print("length elements:",len(elements), 'elements: ',elements)
            # self.driver.quit()
        except (NoSuchElementException):
            self.driver.quit()
            # return False
        return len(elements)!=0


    def comments(self):
        # element=self.driver.find
        pass


if __name__=='__main__':
    r=ReviewRequest()
    r.hasRequest()

