from dao.DB_orm import db
from models.ORM_models import Reimbursement
from sqlalchemy import delete, engine


def deleteRequestByReimbursementId(id):
    requests=Reimbursement.query.filter_by(reimbursement_id=id).first()
    if requests is not None:
        Reimbursement.query.filter_by(reimbursement_id=id).delete()
        db.session.commit()
        return f"Request number {id} Deleted Successfully"
    else:
        return "No Data To Delete"