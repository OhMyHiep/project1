from dao.DB_orm import db
from models.ORM_models import Employee 
import hashlib


def loginUser(loginData):
    employee=Employee.query.filter_by(username=loginData.get('username')).first()
    # print('\n',employee.password,"\n")

    if employee and validatePassword(loginData.get("password1"),employee.password):
        return employee
    return None





def validatePassword(input_password,queried_password)->bool:
    if hashlib.sha256(input_password.encode("utf-8")).hexdigest() == queried_password:
        return True
    return False
    



