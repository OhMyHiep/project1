import re

from sqlalchemy import true
from dao.DB_orm import db
from flask_login import current_user
from models.ORM_models import Reimbursement

def addReimbursement(data):
    print(f"description={data.get('description')},amount={data.get('amount')},status='pending',employee_id={current_user.employee_id},category_id={data.get('category_id')}") 
    reimbursement=Reimbursement(description=data.get('description'),amount=data.get('amount'),status='pending',employee_id=current_user.employee_id,category_id=data.get('category_id'))
    db.session.add(reimbursement)
    db.session.commit()
    db.session.refresh(reimbursement)
    return reimbursement if reimbursement else None


def viewRequestByEmployeeId(id):
    requests=Reimbursement.query.filter_by(employee_id=id).all()
    # requests=db.session.query(Reimbursement,Category).filter_by(employee_id=id).join(Category, Reimbursement.category_id == Category.category_id)
    # req_data=requests.all()
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
        if requests.status=="pending":
            Reimbursement.query.filter_by(reimbursement_id=id).update({'status': "Cancelled"})
            db.session.commit()
            return f"Request number {id} Cancelled Successfully"
        if requests.status=="Cancelled":
            return "Record is alrady Cancelled"
        if requests.status=="Accepted":
            return "Can Not Cancel Accepted Request"
        else:
            return f"Can Not Cancel {requests.status} Request"
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
    if reimbursement and reimbursement.employee_id!=current_user.employee_id and isManager() and validateComments(comments):
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


# validation functions
def isValidReimbursement(data):
    # print(f"data exists: {dataExistForAdding(data)}")
    return dataExistForAdding(data) and validateDescription(data.get('description')) and validateAmount(amount=data.get('amount'))


def validateDescription(description):
    if re.findall('(\d*[a-zA-Z]+\d*)+',description):
        description=description.strip()
        return len(description)>1 and len(description)<=50 
    return False


def validateAmount(amount):
    try:
        amount=float(amount)
        if (amount)>0 and (amount)<=1000:
            return True
        return False
    except ValueError:
        return False
    


def validateComments(comments):
    if re.findall('(\d*[a-zA-Z]+\d*)+',comments):
        comments=comments.strip()
        return len(comments)>1 and len(comments)<=100 
    print("Invalid Comments To Save in Database")
    return False


def dataExistForAdding(requestData):
     return requestData and 'description' in requestData and 'amount' in requestData and 'category_id' in requestData
        

def dataExistToAlterRequest(requestData):
    return requestData and 'reimbursement_id' in requestData and 'comments' in requestData and 'status' in requestData
