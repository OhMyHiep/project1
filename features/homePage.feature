Feature: Test User will go to homepage after login
    
    Scenario Outline: User want to see the Homepage
        Given the user is on the login page
        When the user input username <username>
        When user input password <password>
        When the user click submit button
        Then the user can see homepage

        Examples: login
            |   username    |   password    |
            |   username    |   password    |
            # |   testing     |   testing     |


    Scenario Outline: User Want to see add Reimbursement Page
        Given the user is on the login page
        When the user input username <username>
        When user input password <password>
        When the user click submit button
        When User click on Add New Reimbursement button
        Then User can see the Reimbursement page

        Examples: login
            |   username    |   password    |
            |   username    |   password    |


    Scenario Outline: User Want to Add New Reimbursement
        Given the user is on the login page
        When the user input username <username>
        When user input password <password>
        When the user click submit button
        When User click on Add New Reimbursement button
        When User selects the Reimbursement Type <type>
        When User enter valid description <description>
        When User enter valid amount <amount>
        When User click on submit Reimbursement button
        Then User moved back to the homepage

        Examples: login
            |   username    |   password    |   type    |   description                     |   amount  |
            |   username    |   password    |   travel  |   Travel expense for behave test  |   140     |

        #Examples: new Reimbursement Request
            


    Scenario Outline: view Prveious Reimbursement
        
        Given the user is on the login page
        When the user input username <username>
        When user input password <password>
        When the user click submit button
        When User click on View Previous Reimbursements button
        Then User can see all prvious requests

        Examples: login
            |   username    |   password    |
            |   username    |   password    |


    Scenario Outline: view Delete Reimbursement
        
        Given the user is on the login page
        When the user input username <username>
        When user input password <password>
        When the user click submit button
        When User click on Delete Reimbursement Requests button
        Then User can see Deleteable prvious requests

        Examples: login
            |   username    |   password    |
            |   username    |   password    |


    Scenario Outline: user want to cencel Reimbursement
        
        Given the user is on the login page
        When the user input username <username>
        When user input password <password>
        When the user click submit button
        When User click on View Previous Reimbursements button
        When User click on cancel button of pending request
        Then update the request status to cancel 

        Examples: login
            |   username    |   password    |
            |   username    |   password    |

    

    Scenario Outline: user want to delete Reimbursement
        
        Given the user is on the login page
        When the user input username <username>
        When user input password <password>
        When the user click submit button
        When User click on Delete Reimbursement Requests button
        When User click on Delete button of pending or cancelled request
        Then delete the request from table

        Examples: login
            |   username    |   password    |
            |   username    |   password    |