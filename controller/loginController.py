
from service import LoginService
from flask import render_template
from flask_login import login_user, current_user
from models import UserDto 





def login(loginData):
    user_info=LoginService.loginUser(loginData)
    if (len(user_info)==0):
        return "failed login"
    login_user(UserDto.User(user_info[0][0],user_info[0][1],user_info[0][2],user_info[0][3]),remember=True)
    return render_template("home.html", user=current_user)
   





def loginPage():
    return render_template("login.html",user=current_user)