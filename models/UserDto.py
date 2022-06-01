
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,user_id,firstName,lastName,email):
        self.user_id=user_id
        self.firstName=firstName
        self.lastName=lastName
        self.email=email
        
    def __repr__(self):
        return f" first: {self.firstName} + last:{self.lastName} + email: {self.email}"

    def isValidUser(self)-> bool:
        if (len(self.firstName)>12 or len(self.firstName)<2):
            return False
        if (len(self.lastName)>12 or len(self.lastName)<2):
            return False
        if('@' not in self.email):
            return False
        return True
    
    def get_id(self):
           return int(self.user_id)