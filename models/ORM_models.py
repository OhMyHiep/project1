from typing import List
from urllib.request import Request
from website import db
from flask_login import UserMixin
from dataclasses import dataclass


EmployeRole=db.Table("EmployeRole",
    db.Column('employee_id',db.Integer,db.ForeignKey('employee.employee_id')),
    db.Column('role_id', db.Integer,db.ForeignKey('role.role_id'))
)

@dataclass
class Role(db.Model):
    role_id:int
    roleTitle:str

    role_id=db.Column(db.Integer,primary_key=True)
    roleTitle= db.Column(db.String(50))

    def get_id(self):
        return int(self.role_id)



@dataclass
class Reimbursement(db.Model):
    reimbursement_id:int
    description:str
    amount:int
    status:str
    comments:str
    employee_id:int
    category_id:int

    reimbursement_id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(50))
    amount=db.Column(db.Integer)
    status=db.Column(db.String(50))
    comments=db.Column(db.String(100))
    employee_id=db.Column(db.Integer, db.ForeignKey('employee.employee_id'))
    category_id=db.Column(db.Integer, db.ForeignKey('category.category_id'))

    def get_id(self):
        return int(self.reimbursement_id)


@dataclass
class Employee(db.Model,UserMixin):
    employee_id:int
    firstName:str
    lastName:str
    email:str
    username:str
    password:str
    roles: List[Role]
    reimbursements: List[Reimbursement]

    employee_id=db.Column(db.Integer,primary_key=True)
    firstName=db.Column(db.String(50))
    lastName=db.Column(db.String(50))
    email=db.Column(db.String(50))
    username=db.Column(db.String(50))
    password=db.Column(db.String(255))
    roles= db.relationship('Role',secondary=EmployeRole,backref="employees")
    reimbursements=db.relationship('Reimbursement',backref='employee')
    __table_args__ = (db.UniqueConstraint('email',"username", name='unique_Email_username'),)
    
    def get_id(self):
        return int(self.employee_id)


@dataclass
class Category(db.Model):
    category_id:int 
    categoryName:str
    requests=List[Request]

    category_id=db.Column(db.Integer,primary_key=True)
    categoryName=db.Column(db.String(50))
    requests=db.relationship('Reimbursement')

    def get_id(self):
        return int(self.category_id)