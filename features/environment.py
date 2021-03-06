from behave.runner import Context
from selenium import webdriver
from POM.Login import Login
from POM.reviewRequest import ReviewRequest
from POM.Homepage import HomePage
from POM.addReimbursement import ReimbursementPage
from POM.NavBar import NavBar
import os 

def before_all(context: Context):
    # We need to add a driver to the context
    sachinPath="/Users/Sachin/projects/project1/drivers/chromedriver.exe"
    hiepPath="/Users/hiephuynh/Documents/revature/project1/drivers/chromedriver"
    if os.path.isfile(sachinPath):
        context.driver = webdriver.Chrome(sachinPath)
    else:
        context.driver = webdriver.Chrome(hiepPath)
    # context.driver.get("https://www.google.com")
    # We need to add all POMS to the context
    print(f'\n context driver here: {context.driver}\n')
    context.login=Login(context.driver)
    context.reviewRequest=ReviewRequest(context.driver)
    context.homepage=HomePage(context.driver)
    context.reimbursementPage=ReimbursementPage(context.driver)
    context.navBar=NavBar(context.driver)
    # We add an implicit wait to work with latency issues
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    # This will make sure at the end of a behave test all the drivers are closed
    context.driver.quit()
