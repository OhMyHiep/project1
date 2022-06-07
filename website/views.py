from turtle import done
from flask import Blueprint, jsonify, make_response, request, render_template
from flask_login import login_required, current_user
from controller import EmployeeController, CategoryController, ReimbursementController
import hashlib
import json 
from sqlalchemy.ext.serializer import loads, dumps


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

    EmployeeController.getEmployeeById(current_user.employee_id)
    return " "
    
@login_required    
@views.route('/reimbursement',methods=['GET','POST','DELETE'])
def handleReimbursements():
    if request.method=="GET":
        allRequests=ReimbursementController.getAllReimbursements(current_user.employee_id)
        print(allRequests)
        return allRequests
    if request.method=="POST":
        return ReimbursementController.addReimbursement(request.form)
    if request.method=="DELETE":
        #yet to implement get id from webpage of selected
        #reimbursement request
        #it will return a status string to show on a alert box
        #return ReimbursementController.cancelReimbursement(9)
        #return ReimbursementController.deleteReimbursement(remb_id)
        
        data=ReimbursementController.getReimbursementsByStatus("Cancelled")
        for i in data:
            print(f"Caneled data {i.reimbursement_id} {i.category_id}")
        return "done"
        