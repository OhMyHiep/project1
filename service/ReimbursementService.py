import re
from dao.DB_orm import db
from flask_login import current_user
from models.ORM_models import Reimbursement,Category

def addReimbursement(data):
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
    if(len(data)==0):
        print("No Reimbursement Data To Validate")
        return False
    return validateDescription(data.get('description')) and validateAmount(amount=data.get('amount'))

def validateDescription(description):
    if re.findall('[A-Za-z0-9]',description):
        description=description.strip()
        return len(description)>1 and len(description)<=50 
    return False

def validateAmount(amount):
    if int(amount)>0 and int(amount)<=1000:
        return True
    return False

def validateComments(comments):
    if re.findall('[a-zA-Z0-9$@.#,+!%&-]',comments):
        comments=comments.strip()
        return len(comments)>1 and len(comments)<=50 
    print("Invalid Comments To Save in Database")
    return False
