import time
from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException 
import logging


req_id=""
del_id=""

@when(u'the user click submit button')
def submit(context):
    context.login.submit().click()

@then(u'the user can see homepage')
def homepage(context):
    assert context.homepage.getTitle()=="Home"



@when(u'User click on Add New Reimbursement button') 
def addNewReimbursement(context):
    context.homepage.AddRequestBtn().click() 

@then(u'User can see the Reimbursement page')
def reimbursement(context):
    assert context.reimbursementPage.getTitle() =="Reimbursement"


@given(u'User is on the homepage')
def homepageTitle(context):
    context.homepage.getHomePage()

@when(u'User click on View Previous Reimbursements button')
def viewReimbursementsBtn(context):
    context.homepage.ViewAllBtn().click()

@then(u'User can see all prvious requests')
def viewAllReimbursements(context):
    assert context.homepage.ViewAllContainer().is_displayed() == True



@when(u'User click on Delete Reimbursement Requests button')
def viewReimbursementsBtn(context):
    context.homepage.DeleteRequestBtn().click()    


@then(u'User can see Deleteable prvious requests')
def viewAllReimbursements(context):
    assert context.homepage.DeleteContainer().is_displayed() == True


@when(u'User click on cancel button of pending request')
def clickCancelBtn(context):
    global req_id
    try:
        req_id = context.homepage.getPendingRequestId().text
        print(req_id)
        context.homepage.cancelBtn().click()
        time.sleep(1)
        context.homepage.clickAlertbox()
    except (NoSuchElementException) as e:
        print("No Element Found ")


@then(u'update the request status to cancel')
def updateStatus(context):
    context.homepage.refreshPage()
    time.sleep(2) 
    context.homepage.ViewAllBtn().click()
    status = context.homepage.findReqStatus(req_id).text
    print(status)
    assert status=='Cancelled'



@when(u'User click on Delete button of pending or cancelled request')
def clickDeleteBtn(context):
    global del_id
    try:
        del_id = context.homepage.getRequestId("Cancelled").text
        print(del_id)
        context.homepage.deleteBtn(del_id).click()
        time.sleep(1)
        context.homepage.clickAlertbox()
    except (NoSuchElementException) as e:
        print("No Element Found ")
        

@then(u'delete the request from table')
def updateTable(context):
    context.homepage.refreshPage()
    time.sleep(1) 
    context.homepage.DeleteRequestBtn().click()
    try:
        context.homepage.findDeletedRecord(del_id)
        assert False
    except NoSuchElementException: 
        assert True


@when(u'User selects the Reimbursement Type {type}')
def selectReqType(context,type):
    context.reimbursementPage.selectCategory(type)

@when(u'User enter valid description {description}')
def enterDescription(context,description):
    context.reimbursementPage.description().send_keys(description)

@when(u'User enter valid amount {amount}')
def enterAmount(context,amount):
    context.reimbursementPage.amount().send_keys(amount)

@when(u'User click on submit Reimbursement button')
def submitBtn(context):
    context.reimbursementPage.submitBtn().click()

@then(u'User moved back to the homepage')
def currentPage(context):
    assert context.reimbursementPage.getCurrentPageTitle() =="Home"

        
        
        