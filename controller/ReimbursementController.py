from service import ReimbursementService
from flask_login import current_user
from flask import url_for, redirect

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


>>>>>>> 21d9441 (minor changes)
