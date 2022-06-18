from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u'I\'m on reviewRequest.html and request exists to review')
def step_impl(context):
    # context.reviewRequest.login.loginUser('testing','testing')
    context.reviewRequest.getReviewRequestPage()

@when(u'I input{comments}')
def step_impl(context,comments):
    context.reviewRequest.getComments().send_keys(comments)


@when(u'I click{button} to submit')
def step_impl(context,button):
    context.reviewRequest.getButton(button.strip()).click()
    WebDriverWait(context.driver, 30).until(EC.invisibility_of_element_located((By.ID,context.reviewRequest.request_id)))


@then(u'the page will remove it if comments are valid')
def step_impl(context):
    assert len(context.reviewRequest.driver.find_elements(By.ID,f'{context.reviewRequest.request_id}'))==0


@when(u'I click {button} to submit invalid comments')
def step_impl(context,button):
    context.reviewRequest.getButton(button.strip()).click()
    WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.ID,context.reviewRequest.request_id)))


@then(u'the page will not remove the reimbursement request')
def step_impl(context):
    assert len(context.reviewRequest.driver.find_elements(By.ID,f'{context.reviewRequest.request_id}'))==1
