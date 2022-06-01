

class Login:

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def isValidLogin(self)->bool:
        if(self.username is None or self.password is None):
            return False
        # if (len(self.username)<5 or len(self.username)>20):
        #     return False
        # if (len(self.password)<5):
        #     return False
        return True
