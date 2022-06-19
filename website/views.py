from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
from controller import EmployeeController, CategoryController, ReimbursementController
import json

views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    categories=CategoryController.getAllCategories()
    allRequests=ReimbursementController.getAllReimbursements(current_user.employee_id)
    jsonify(allRequests)
    return render_template('home.html',employee=current_user,categories=categories,allRequests=allRequests)
    

@views.route('/sample-test',methods=['GET','POST'])
def testing_db():
    1/0
    return ''

    

@views.route('/reimbursement',methods=['GET','POST','DELETE'])
@login_required
def handleReimbursements():
    if request.method=="GET":
        allRequests=ReimbursementController.getAllReimbursements(current_user.employee_id)
        print(allRequests)
        return jsonify(allRequests)
    if request.method=="POST":
        #print(f"Post Method{request.form}" )
        return ReimbursementController.addReimbursement(request.form)
    if request.method=="DELETE":
        #jsonify(ReimbursementController.getReimbursementsByStatus("Cancelled"))
        data=json.loads(request.data)
        req_id=data['req_id']
        #print(req_id)
        return jsonify(ReimbursementController.cancelReimbursement(int(req_id)))

@views.route('/delreimbursement',methods=['DELETE'])
@login_required
def deleteReimbursement():
    data=json.loads(request.data)
    req_id=data['req_id']
    print(req_id)
    return jsonify(ReimbursementController.deleteReimbursement(int(req_id)))


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
