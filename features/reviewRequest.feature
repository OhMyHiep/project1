Feature: Testing accepting or rejecting a Reimbursement Request

    Test the functions of inputs on this page

        Scenario Outline: input request with comments and click accept or reject button
            Given I'm on requestReimbursement.html and request exists to review
            When I input <comments> 
            When I click the accept or reject button
            Then the page will give a response

            Examples: Rejecting Reimbursement requests with proper input
            |   comments    |
            |   gibberish   |
            |   reject      |
            |   Testing     |

            Examples: Accepting Reimbursement request
            |   comments    |
            |   accept      |
            |   ok          |

            Examples: blank comments
            |   comments    |
            |               |
