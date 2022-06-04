from service import SignUpService
from flask import render_template, redirect, url_for
from flask_login import current_user

def signUp(formData):
    if(SignUpService.isValidRegistration(formData)):
       result=SignUpService.signUp(formData)
       return "failed Registration" if result==None else redirect(url_for("auth.login"))
    return render_template("sign-up.html", employee=current_user)

    