from sre_parse import CATEGORIES
from service import ReimbursementService
from flask_login import current_user
from flask import url_for, redirect

def addReimbursement(data):
    reimbursement=ReimbursementService.addReimbursement(data)
    return redirect(url_for('views.home')) if reimbursement else "failed add"

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