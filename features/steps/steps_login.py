from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 

@given(u'the user is on the login page')
def loginPpage(context):
    context.login.getLoginPage()

@when(u'the user input username {username}')
def username(context,username):
    context.login.username().send_keys(username)

@when(u'user input password {password}')
def password(context,password):
    context.login.password().send_keys(password)

@when(u'the user click submit')
def submit(context):
    context.login.submit().click()
   

@then(u'the nav bar will display {button} but only {button2} for managers')
def compare(context,button,button2):
    try:
       element= context.driver.find_element(By.ID,button2)
       assert element and context.driver.find_element(By.ID,button) #both buttons exits for managers 
    except (NoSuchElementException) as e:
        assert context.driver.find_element(By.ID,button) and e #one button exist for employee


@when(u'the user input username{username}')
def username(context,username):
    context.login.username().send_keys(username)

@when(u'user input password{password}')
def password(context,password):
    context.login.password().send_keys(password)

@when(u'user click submit')
def submit(context):
    context.login.submit().click()

@then(u'user will not login')
def compare(context):
    assert context.driver.find_element(By.TAG_NAME,"body").text =='failed login'