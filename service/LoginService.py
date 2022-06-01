from dao import LoginDao


def isValidLogin(loginData)->bool:
    return validateUsername(loginData.get("username")) and validateUsername(loginData.get("password1"))

def loginUser(loginData):
    return LoginDao.getUserIDBylogin(loginData.get("username"),loginData.get("password1"))

def validateUsername(username)->bool:
    if username is not None:
        username=username.strip()
        return len(username)>5 and len(username)<20
    return False

def validatePassword(password)->bool:
    if password is not None:
        password=password.strip()
        return password is not None and len(password)>5
    return False
    


