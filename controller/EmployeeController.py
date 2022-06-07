
from service import EmployeeService


def getEmployeeById(emp_id):
    employee=EmployeeService.getEmployeeById(emp_id)
    print("\nEmployee: ",employee,"\n")
    return employee


def addEmployee():
    employee=EmployeeService.addEmployee()
    