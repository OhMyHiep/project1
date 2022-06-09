from dao.DB_orm import db
from models.ORM_models import Employee, Reimbursement


def getEmployeeById(id):
    employee=Employee.query.filter_by(employee_id=id).first()
    return employee



    