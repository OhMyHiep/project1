from website import db
from flask_login import UserMixin

EmployeRole=db.Table("EmployeRole",
    db.Column('employee_id',db.Integer,db.ForeignKey('employee.employee_id')),
    db.Column('role_id', db.Integer,db.ForeignKey('role.role_id'))
)

class Role(db.Model):
    role_id=db.Column(db.Integer,primary_key=True)
    roleTitle= db.Column(db.String(50))


class Employee(db.Model,UserMixin):
    employee_id=db.Column(db.Integer,primary_key=True)
    firstName=db.Column(db.String(50))
    lastName=db.Column(db.String(50))
    email=db.Column(db.String(50))
    username=db.Column(db.String(50))
    password=db.Column(db.String(255))
    roles= db.relationship('Role',secondary=EmployeRole,backref="employees")
    requests=db.relationship('Request')
    __table_args__ = (db.UniqueConstraint('email',"username", name='unique_Email_username'),
                     )


class Category(db.Model):
    category_id=db.Column(db.Integer,primary_key=True)
    categoryName=db.Column(db.String(50))
    requests=db.relationship('Request')

class Request(db.Model):
    request_id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(50))
    amount=db.Column(db.Integer)
    status=db.Column(db.String(50))
    comments=db.Column(db.String(50))
    employee_id=db.Column(db.Integer, db.ForeignKey('employee.employee_id'))
    category_id=db.Column(db.Integer, db.ForeignKey('category.category_id'))