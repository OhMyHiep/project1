from dao.DatabaseUtil import *
import hashlib

def insertLogin(connection,username,password):
    sql="""INSERT INTO Login (username,password) VALUES (%s,%s) RETURNING login_id;"""
    result=executeQuery(connection,sql,username,hashlib.sha256(password.encode("utf-8")).hexdigest())
    return result[0][0] if result is not None else result

def getUserIDBylogin(username,password):
    sql="""SELECT user_id, firstname, lastname, email
    FROM login l join users u ON l.login_id = u.login_id
    WHERE l.username=%s AND l.password=%s;"""
    result=executeSimpleQuery(sql,username,hashlib.sha256(password.encode("utf-8")).hexdigest())
    print(f"(user info :{result})")
    return result 