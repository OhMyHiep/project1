from flask import Blueprint, redirect, request, url_for
from controller import SignUpController
from controller import loginController
from flask_login import login_required, logout_user


auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        return loginController.login(request.form)
    return loginController.loginPage()

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    return SignUpController.signUp(request.form)
    # return render_template("sign-up.html")
 
