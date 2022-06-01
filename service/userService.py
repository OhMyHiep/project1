from dao import userDao

def getUserbyId(user_id):
    return userDao.getUserById(user_id)