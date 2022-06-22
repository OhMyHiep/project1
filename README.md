# Reimbursement Expense Apllication


## Description
create an expense reimbursement system for a small group. This program will allow employees to create reimbursement requests for their business expenditures, while also providing a way to track the amount of money they have spent.


### Key Features
- Employees will be able to:
    - Login to their account with a unique username and a password
    - Submit reimbursement requests with a description and a dollar amount 
    - Have categories for your requests
    - See ongoing and previous requests
    - Cancel ongoing requests

- Managers will be able to:
    - Have the same options as an employee
    - Approve / decline reimbursement requests
    - provide a reason why

### Business Rules
- Employees reimburesment requests must be between $1 and $1000 per request
- Employee reimburesment request comments must be no longer than 100 characters
- Employee reimbursement requests must be in numeric form

### Usage
- ### Assumption: 
    - you should have your own database as the one in this project may no longer be availibile
    - make sure python3 is installed
    - clone the poject 
    ```
    git clone <this project url>
    ```
- install pip
```
python3 -m pip install --user --upgrade pip
```
- install virtual environment
```
python3 -m pip install --user virtualenv
```
- create virtual environment
```
python3 -m venv env
```
- go into the enivironment
```
cd env/bin
```
- actitvate the environment
```
source activate
```
- install the dependencies 
```
pip install sqlalchemy
pip install flask
pip install flask_login
pip install flask_sqlalchemy
pip install psycopg2
pip install sqlalchemy
pip install sqlalchemy_utils
pip install pytest
```
- go to project root folder
```
cd ../..
```
- run the project
```
python main.py
```
- the application will be availible on http://localhost:5000 

### Credits: 
https://github.com/sachingarg5
https://github.com/OhMyHiep
 

