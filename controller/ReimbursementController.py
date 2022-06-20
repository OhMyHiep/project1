from models.ORM_models import Employee, Reimbursement
from service import ReimbursementService
from flask_login import current_user
from flask import render_template, url_for, redirect
from controller import CategoryController

def addReimbursement(data):
    if(ReimbursementService.isValidReimbursement(data)):
        reimbursement=ReimbursementService.addReimbursement(data)
        return render_template("home.html", employee=current_user, reimbursement=reimbursement) if reimbursement else "failed add"
    return "Wrong input for Reimbursement Request"
    
    
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
    if ReimbursementService.dataExistToAlterRequest(requestData):
        return ReimbursementService.alterReimbursement(requestData)
    return {"response":"bad request", "status":400}

def getReimbursementView():
    categories=CategoryController.getAllCategories()
    return render_template('requestReimbursement.html',categories=categories,employee=current_user)


def getManagerReimbursementView():
    reimbursements=ReimbursementService.managerViewRequestByStatus({'status':'pending'})
    return render_template('reviewRequest.html',reimbursements=reimbursements,employee=current_user)