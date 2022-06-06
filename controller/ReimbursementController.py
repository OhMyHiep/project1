from sre_parse import CATEGORIES
from service import ReimbursementService
from flask_login import current_user
from flask import url_for, redirect

def addReimbursement(data):
    reimbursement=ReimbursementService.addReimbursement(data)
    return redirect(url_for('views.home')) if reimbursement else "failed add"
