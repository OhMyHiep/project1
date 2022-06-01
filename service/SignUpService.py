from models.UserDto import *
from models.signUp import *
from dao import LoginDao
from dao import userDao
from dao import DatabaseUtil
import re

def isValidRegistration(formData):
    if(len(formData)==0):
        print("no form data")
        return False
    em=(validateEmail(formData.get("email")))
    fn=validateFirstName(formData.get("firstName")) 
    ln=validateLastName(formData.get("lastName"))
    un=validateUsername(formData.get("username"))
    p=validatePassword(formData.get("password1"),formData.get("repeat-password"))
    print("fn:",fn," ln:",ln, " un:",un," p:",p, " em:",em)
    return validateEmail(formData.get("email")) and validateFirstName(formData.get("firstName")) and validateLastName(formData.get("lastName")) and validateUsername(formData.get("username")) and validatePassword(formData.get("password1"),formData.get("repeat-password"))


def signUp(formData):
    connection = DatabaseUtil.getConnection()
    login_id=LoginDao.insertLogin(connection,formData.get("username").strip(),formData.get("password1").strip())
    user_id=userDao.insertUser(connection,formData.get("firstName").strip(),formData.get("lastName").strip(),formData.get("email").strip(),login_id)
    DatabaseUtil.commit(connection)
    DatabaseUtil.close(connection)
    return user_id
    


def validateUsername(username)->bool:
    if re.findall('^(?=.{6,19}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._ ]+(?<![_.])$',username):
        username=username.strip()
        return len(username)>5 and len(username)<20 and " " not in username
    print("username false")
    return False


def validatePassword(password,password2)->bool:
    if password and password2:
        password=password.strip()
        password2=password2.strip()
        return len(password)>5 and len(password)<20 and password==password2
    print("password false")
    return False


def validateFirstName(firstName):
    if re.findall('[A-Za-z]',firstName):
        firstName=firstName.strip()
        return len(firstName)>1 and len(firstName)<15 and " " not in firstName 
    return False


def validateLastName(lastName):
    if re.findall('[A-Za-z]',lastName):
        lastName=lastName.strip()
        return len(lastName)>1 and len(lastName)<15 and " " not in lastName 
    print("last name false")
    return False


def validateEmail(email):
    if re.findall('^(?![_.])([A-Za-z0-9])(?!.*[_.]{2})+([.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+(?<![_.])$',email):
        return ('@' in email)
    print("email false")
    return False

    