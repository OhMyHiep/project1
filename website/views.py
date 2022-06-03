from flask import Blueprint, jsonify, request
from dao.DatabaseUtil import *
from flask_login import login_required, current_user
from controller import MessageController, EmployeeController

import json


views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
       return MessageController.saveMessage(request.form)
    return MessageController.getUserMessages(current_user)
    

@views.route('/delete-message', methods=['POST'])
@login_required
def deleteMessage():
    msgData=json.loads(request.data)
    print('\n',msgData)
    deleted=MessageController.deleteMessage(msgData['msg_obj'])
    return jsonify({})

@views.route('/sample-test')
def testing_db():
    # EmployeeController.addEmployee()
    EmployeeController.getEmployeeById()
    return " "
    