from behave.runner import Context
from selenium import webdriver
from POM.Login import Login
from POM.reviewRequest import ReviewRequest
from POM.Homepage import HomePage
from POM.addReimbursement import ReimbursementPage
import logging

def before_all(context: Context):
    # We need to add a driver to the context
    context.driver = webdriver.Chrome("/Users/Sachin/projects/project1/drivers/chromedriver.exe")
    # context.driver.get("https://www.google.com")
    # We need to add all POMS to the context
    context.config.setup_logging(filename="debug.log", level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    print(f'\n context driver here: {context.driver}\n')
    context.login=Login(context.driver)
    context.reviewRequest=ReviewRequest(context.driver)
    context.homepage=HomePage(context.driver)
    context.reimbursementPage=ReimbursementPage(context.driver)
    # We add an implicit wait to work with latency issues
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    # This will make sure at the end of a behave test all the drivers are closed
    context.driver.quit()
