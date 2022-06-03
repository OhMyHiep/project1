
from service import LoginService
from flask import render_template
from flask_login import login_user, current_user
from models import UserDto 





def login(loginData):
    employee=LoginService.loginUser(loginData)
    if not employee:
        return "failed login"
    login_user(employee,remember=True)
    return render_template("home.html", employee=current_user)
   



def loginPage():
    return render_template("login.html",employee=current_user)