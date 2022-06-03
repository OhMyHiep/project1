from dao.DB_orm import db 

def addEmployee(employee):
    db.session.add(employee)