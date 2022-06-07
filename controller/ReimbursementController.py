from sre_parse import CATEGORIES
from service import ReimbursementService,ViewAllRequestService,DeleteRequestService
from flask_login import current_user
from flask import url_for, redirect

def addReimbursement(data):
    reimbursement=ReimbursementService.addReimbursement(data)
    return redirect(url_for('views.home')) if reimbursement else "failed add"

def getAllReimbursements(emp_id):
    allRequests=ViewAllRequestService.viewRequestByEmployeeId(emp_id)
    return allRequests

def deleteReimbursement(remb_id):
    status=DeleteRequestService.deleteRequestByReimbursementId(remb_id)
    return status