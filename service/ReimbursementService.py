from dao.DB_orm import db
from flask_login import current_user
from models.ORM_models import Reimbursement

def addReimbursement(data):
    reimbursement=Reimbursement(description=data.get('description'),amount=data.get('amount'),status='pending',employee_id=current_user.employee_id,category_id=data.get('category_id'))
    db.session.add(reimbursement)
    db.session.commit()
    db.session.refresh(reimbursement)
    return reimbursement if reimbursement else None