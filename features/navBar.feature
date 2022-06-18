Feature: navigation bar can redirect to other pages

    Scenario Outline: clicking navigation button
        Given I have notlogged in
        When I click a navigation <button>
        Then I will be redirected to <page>

        Examples: 
        |   button  |   page    |
        |   signUp  |   Sign Up |
        |   login   |   Login   |
        
    Scenario Outline: I'm logged in as a manager to unlock all navigation buttons
        Given I'm logged in as a manager to unlock all navigation buttons
        When I click a navigation <button>
        Then I will be redirected to <page>

        Examples:
        |   button              |   page                |            
        |   review-requests     |   Review Requests     |
        |   home                |   Home                |     
        |   reimbursement       |   Reimbursement       |       