from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
from controller import EmployeeController, CategoryController, ReimbursementController


views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    categories=CategoryController.getAllCategories()
    
    return render_template('home.html',employee=current_user,categories=categories)
    

@views.route('/sample-test')
def testing_db():
    # EmployeeController.addEmployee()
    return jsonify(EmployeeController.getEmployeeById())

    
@login_required    
@views.route('/reimbursement',methods=['GET','POST','DELETE'])
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



@login_required
@views.login.route('reimbursement/cancel')
def rejectReimbursement():
    reimbursement_id=request.args.get("reimbursement_id")
    ReimbursementController.rejectReimbursement(reimbursement_id)