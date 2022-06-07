from dao.DB_orm import db
from models.ORM_models import Employee, Reimbursement


def getEmployeeById(id):
    employee=Employee.query.filter_by(employee_id=id).first()
    return employee


def addEmployee():
    employee= Employee(firstName='firstName',lastName='lastName',email='email@this.com',username='username',password='password')
    db.session.add(employee)
    db.session.commit()
    db.session.refresh(employee)
    return employee

    