class SignUp:

    def __init__(self,username,password,password2):
        self.username=username
        self.password=password
        self.password2=password2

    def isValidSignUp(self)->bool:
        if(self.username is None or self.password is None):
            return False
        if(self.password!=self.password2):
            return False
        if (len(self.username)<5 or len(self.username)>20):
            return False
        if (len(self.password)<5 or len(self.password)>20):
            return False
        return True