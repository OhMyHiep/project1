from service import MessageService
from flask import flash, render_template
from flask_login import current_user


def saveMessage(msgData):
    message_id=MessageService.saveMessage(msgData)
    messageList=MessageService.getMessagesByUserId(msgData.get('user_id'))
    if not message_id:
        flash("message failed to save",category="error")
    flash("message added",category="success")
    # print(messageList)
    return render_template("home.html",user=current_user, message=messageList)


def getUserMessages(current_user):
    messageList=MessageService.getMessagesByUserId(current_user.user_id)
    return render_template("home.html",user=current_user, message=messageList)
    

def deleteMessage(msgData):
    if current_user.user_id == msgData['user_id']:
        return MessageService.deleteMessage(msgData)