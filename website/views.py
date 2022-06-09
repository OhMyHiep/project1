from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
from controller import EmployeeController, CategoryController, ReimbursementController
import json

views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    
    return render_template('home.html',employee=current_user)
    

@views.route('/sample-test',methods=['GET','POST'])
def testing_db():
    # EmployeeController.addEmployee()
    requestData=json.loads(request.data)
    print("\n",type(requestData),"\n")
    return jsonify({"id":"testing","status":"returning"})

    

@views.route('/reimbursement',methods=['GET','POST','DELETE'])
@login_required
def handleReimbursements():
    if request.method=="GET":
        allRequests=ReimbursementController.getAllReimbursements(current_user.employee_id)
        print(allRequests)
        return jsonify(allRequests)
    if request.method=="POST":
        return ReimbursementController.addReimbursement(request.form)
    if request.method=="DELETE":
        #yet to implement get id from webpage of selected
        #reimbursement request
        #it will return a status string to show on a alert box
        #return ReimbursementController.deleteReimbursement(remb_id)
        return jsonify(ReimbursementController.getReimbursementsByStatus("Cancelled"))


@views.route('/reimbursement/alter',methods=['POST'])
@login_required
def alterReimbursement():
    requestData=json.loads(request.data)
    return jsonify(ReimbursementController.alterReimbursement(requestData))


@views.route('/reimbursement-page')
@login_required
def reimbursementPage():
    return ReimbursementController.getReimbursementView()


@views.route('/review-request')
@login_required
def reviewRequest():
    return ReimbursementController.getManagerReimbursementView()


@views.route('/reimbursement/status',methods=['POST'])
@login_required
def getReimbursementsByStatus():
    requestData=json.loads(request.data)
    return jsonify(ReimbursementController.getReimbursementsByStatus(requestData))
