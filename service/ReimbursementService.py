from dao.DB_orm import db
from flask_login import current_user
from models.ORM_models import Reimbursement

def addReimbursement(data):
    reimbursement=Reimbursement(description=data.get('description'),amount=data.get('amount'),status='pending',employee_id=current_user.employee_id,category_id=data.get('category_id'))
    db.session.add(reimbursement)
    db.session.commit()
    db.session.refresh(reimbursement)
    return reimbursement if reimbursement else None


def viewRequestByEmployeeId(id):
    requests=Reimbursement.query.filter_by(employee_id=id).all()
    if requests is None:
        return "No Previous Request To Show"
    return requests


def deleteRequestByReimbursementId(id):
    requests=Reimbursement.query.filter_by(reimbursement_id=id).first()
    if requests is not None:
        Reimbursement.query.filter_by(reimbursement_id=id).delete()
        db.session.commit()
        return f"Request number {id} Deleted Successfully"
    else:
        return "No Data To Delete"


def cancelRequestByReimbursementId(id):
    requests=Reimbursement.query.filter_by(reimbursement_id=id).first()
    if requests is not None:
        if requests.status=="Pending":
            Reimbursement.query.filter_by(reimbursement_id=id).update({'status': "Cancelled"})
            db.session.commit()
            return f"Request number {id} Cancelled Successfully"
        if requests.status=="Cancelled":
            return "Record is alrady Cancelled"
    else:
        return "No Data To Cancel"

def viewRequestByStatus(status):
    requests=Reimbursement.query.filter_by(status=status).all()
    if requests is None:
        return "No Previous Request To Show"
    return requests