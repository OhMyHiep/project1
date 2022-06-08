from service import ReimbursementService
from flask_login import current_user
from flask import render_template, url_for, redirect
from controller import CategoryController

def addReimbursement(data):
    reimbursement=ReimbursementService.addReimbursement(data)
    return redirect(url_for('views.home')) if reimbursement else "failed add"

<<<<<<< HEAD
def getAllReimbursements(emp_id):
    allRequests=ReimbursementService.viewRequestByEmployeeId(emp_id)
    return allRequests

def deleteReimbursement(remb_id):
    status=ReimbursementService.deleteRequestByReimbursementId(remb_id)
    return status

def cancelReimbursement(remb_id):
    status=ReimbursementService.cancelRequestByReimbursementId(remb_id)
    return status

def getReimbursementsByStatus(status):
    statusRequests=ReimbursementService.viewRequestByStatus(status)
    return statusRequests
=======

def acceptReimbursement(reimbursement_id):
    return ReimbursementService.acceptReimbursement(reimbursement_id)
    

def rejectReimbursement(reimbursement_id):
    return ReimbursementService.rejectReimbursement(reimbursement_id)


<<<<<<< HEAD
>>>>>>> 21d9441 (minor changes)
=======
def getReimbursementView():
    categories=CategoryController.getAllCategories()
    return render_template('requestReimbursement.html',categories=categories,employee=current_user)
>>>>>>> 2596692 (create separate page to submit request, add button to got to submit page)
