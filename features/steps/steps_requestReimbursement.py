from behave import given, when, then


@given(u'I\'m on requestReimbursement.html and request exists to review')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m on requestReimbursement.html and request exists to review')


@when(u'I input {comments}')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I input gibberish')


@when(u'I click the accept or reject button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the accept or reject button')


@then(u'the page will give a response')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the accept or reject button')
