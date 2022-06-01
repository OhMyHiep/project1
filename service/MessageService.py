
from dao import MessageDao

def saveMessage(msgData):
    return MessageDao.saveMessage(msgData.get('msg'),msgData.get('user_id'))



def getMessagesByUserId(user_id):
    return MessageDao.getMessagesByUserId(user_id)


def deleteMessage(msgData):
    return MessageDao.deleteMessage(msgData['message_id'])
    