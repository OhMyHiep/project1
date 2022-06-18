from lib2to3.pgen2 import driver
from behave import given, when, then


@given(u'I have notlogged in')
def step_impl(context):
    context.driver.get('http://127.0.0.1:5000/logout')
    context.navBar.login.getLoginPage()

@when(u'I click a navigation {button}')
def step_impl(context,button):
    context.navBar.getBtnById(button.strip()).click()
    

@then(u'I will be redirected to {page}')
def step_impl(context,page):
    assert context.driver.title==page

@given(u'I\'m logged in as a manager to unlock all navigation buttons')
def step_impl(context):
    context.navBar.login.getLoginPage()
    context.login.loginUser('testing',"testing")


@when(u'I click a navigation{button}')
def step_impl(context,button):
    context.navBar.getBtnById(button.strip()).click()


@then(u'I will be redirected to{page}')
def step_impl(context,page):
    assert context.driver.title==page
