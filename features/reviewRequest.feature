Feature: Testing accepting or rejecting a Reimbursement Request

    Test the functions of inputs on this page

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


            #need different scenarios for alternative path
            # Examples: blank comments
            # |   comments    |   button      |
            # |               |               |
