Feature: Test Login for employees

    Scenario Outline: employee login
        Given the user is on the login page
        When the user input username <username>
        When user input password <password>
        When the user click submit
        Then the nav bar will display <button> but only <button2> for managers

        Examples: login
            |   username    |   password    |   button          |   button2             |
            |   username    |   password    |   reimbursement   |   review-requests     |
            |   testing     |   testing     |   reimbursement   |   review-requests     |

    
       
    Scenario Outline: False login
        Given the user is on the login page
        When the user input username <username>
        When user input password <password>
        When the user click submit
        Then user will not login

        Examples: fail login 
            |   username    |   password    |   button          |   button2             |
            |               |   password    |   reimbursement   |   review-requests     |
            |   testing     |               |   reimbursement   |   review-requests     |
