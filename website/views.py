from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from controller import EmployeeController
import hashlib
import json


views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    return render_template('home.html',employee=current_user)
    

@views.route('/sample-test')
def testing_db():
    # EmployeeController.addEmployee()
    password="password"
    print(hashlib.sha256(password.encode("utf-8")).hexdigest())

    EmployeeController.getEmployeeById()
    return " "
    