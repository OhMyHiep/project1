from models.ORM_models import Employee, Reimbursement
from service import ReimbursementService
from flask_login import current_user
from flask import render_template, url_for, redirect
from controller import CategoryController

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

def getReimbursementsByStatus(requestData):
    statusRequests=ReimbursementService.viewRequestByStatus(requestData)
    return statusRequests


def alterReimbursement(requestData):
    return ReimbursementService.alterReimbursement(requestData)


def getReimbursementView():
    categories=CategoryController.getAllCategories()
    return render_template('requestReimbursement.html',categories=categories,employee=current_user)


def getManagerReimbursementView():
    reimbursements=ReimbursementService.managerViewRequestByStatus({'status':'pending'})
    return render_template('reviewRequest.html',reimbursements=reimbursements,employee=current_user)