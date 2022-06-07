from dao.DB_orm import db
from models.ORM_models import Employee
from models.ORM_models import Reimbursement


def viewRequestByEmployeeId(id):
    requests=Reimbursement.query.filter_by(employee_id=id).all()
    if requests is None:
        return "No Previous Request To Show"
    return requests