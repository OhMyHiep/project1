from dao.DatabaseUtil import *
from dao.DB_orm import db

def insertUser(connection,firstName,lastName,email,login_id):
    sql="""INSERT INTO USERS (firstname, lastname, email, login_id) VALUES(%s,%s,%s,%s) RETURNING user_id;"""
    result=executeQuery(connection,sql,firstName,lastName,email,login_id)
    return result[0][0] if result is not None else result

def getUserById(user_id):
    sql="""SELECT * 
    From users
    WHERE user_id=%s;"""
    return executeSimpleQuery(sql,user_id)

def addEmployee(employee):
    db.session.add(employee)
