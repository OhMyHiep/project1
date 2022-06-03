
from service import EmployeeService


def getEmployeeById():
    employee=EmployeeService.getEmployeeById(1)
    print("\nEmployee: ",employee,"\n")
    return employee


def addEmployee():
    employee=EmployeeService.addEmployee()
    