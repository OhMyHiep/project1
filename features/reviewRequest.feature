Feature: Testing accepting or rejecting a Reimbursement Request

    Test the functions of inputs on this page
        # if there's no request test code throws an exception
        Scenario Outline: input request with comments and click accept or reject button
            Given I'm on reviewRequest.html and request exists to review
            When I input <comments>
            When I click <button> to submit
            Then the page will remove it if comments are valid

            Examples: Rejecting Reimbursement requests with proper input
            |   comments    |   button      |
            |   gibberish   |   Rejected    |
            

            Examples: Accepting reimbursement with proper inputs
            |   comments    |   button      |
            |   second      |   Accepted    |


        Scenario Outline: input request with invalid comments and click accept or reject button
            Given I'm on reviewRequest.html and request exists to review
            When I input invalid <comments> 
            When I click <button> to submit invalid comments
            Then the page will not remove the reimbursement request 

            
            Examples: incorrect comments, blank comments and too long
            |   comments                                                                                                |   button      |
            |                                                                                                           |   Accepted    |
            |   01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890   |   Rejected    |
            |                                                                                                           |   Rejected    |
            |   this is a long comment that's supposed to be over one hundred characters long, very very very very long |   Accepted    |