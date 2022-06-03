from dao.DB_orm import db
from models.ORM_models import Employee



def getEmployeeById(id):
    return Employee.query.filter_by(employee_id=id).first()


def addEmployee():
    employee= Employee(firstName='firstName',lastName='lastName',email='email@this.com',username='username',password='password')
    db.session.add(employee)
    db.session.commit()


    