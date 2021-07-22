# WAP to demonstrate explicite constructor

class employee:
    # This is explicite constructor
    def __init__(self,empID,empName,empSalary):
        print("Inside constructor -- ")
        self.empId = empID
        self.empName = empName
        self.empSalary = empSalary
        print("Constructor END -- ")

    def displayEmployeeDetails(self):
        print("Id = ", self.empId)
        print("Name = ", self.empName)
        print("Salary = ", self.empSalary)
empObject1 = employee(101,'Mr. Pawar',89000)
print(id(empObject1))
print(type(empObject1))
print()
empObject1.displayEmployeeDetails()

print("----------------------------------------------------")

empObject2 = employee(102,'Mr. Khairnar',90000)
print(id(empObject2))
print(type(empObject2))
print()
empObject2.displayEmployeeDetails()
