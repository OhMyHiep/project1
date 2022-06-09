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


def viewRequestByStatus(requestData):
    # print('status' in requestData)
    if 'status' in requestData:
        status=requestData['status']
        requests=Reimbursement.query.filter_by(status=status).all()
        # print(requests)
        if requests is None:
            return "No Previous Request To Show"
        return requests


def alterReimbursement(requestData):
    reimbursement_id=requestData['reimbursement_id']
    comments=requestData['comments']
    status=requestData['status']
    reimbursement=Reimbursement.query.filter_by(reimbursement_id=reimbursement_id).first()
    if reimbursement and reimbursement.employee_id!=current_user.employee_id and isManager():
        reimbursement.status=status
        reimbursement.comments=comments
        db.session.commit()
        db.session.refresh(reimbursement)
        return reimbursement
    return {"status":"404 Not Found"}


def isManager():
    for role in current_user.roles:
        # print(f"\n{role.roleTitle} \n")
        if role.roleTitle=='manager':
            return True
    return False


def managerViewRequestByStatus(requestData):
    requests=viewRequestByStatus(requestData)
    if type(requests)!=str:
        reviewRequest=[r for r in requests if r.employee_id!=current_user.employee_id]
        return reviewRequest
    return requests

    
