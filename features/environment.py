from behave.runner import Context
from selenium import webdriver
from POM.Login import Login
from POM.reviewRequest import ReviewRequest

def before_all(context: Context):
    # We need to add a driver to the context
    context.driver = webdriver.Chrome("/Users/hiephuynh/Documents/revature/project1/drivers/chromedriver")
    # context.driver.get("https://www.google.com")
    # We need to add all POMS to the context
    print(f'\n context driver here: {context.driver}\n')
    context.login=Login(context.driver)
    context.reviewRequest=ReviewRequest(context.driver)
    # We add an implicit wait to work with latency issues
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    # This will make sure at the end of a behave test all the drivers are closed
    context.driver.quit()