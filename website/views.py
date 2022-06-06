from crypt import methods
from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from controller import EmployeeController, CategoryController, ReimbursementController
import hashlib
import json


views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    categories=CategoryController.getAllCategories()
    
    return render_template('home.html',employee=current_user,categories=categories)
    

@views.route('/sample-test')
def testing_db():
    # EmployeeController.addEmployee()
    password="password"
    print(hashlib.sha256(password.encode("utf-8")).hexdigest())

    EmployeeController.getEmployeeById()
    return " "
    
    
@login_required    
@views.route('/reimbursement',methods=['GET','POST'])
def handleReimbursements():
    if request.method=="GET":
        return "place holder for getting requests"
    if request.method=="POST":
        return ReimbursementController.addReimbursement(request.form)