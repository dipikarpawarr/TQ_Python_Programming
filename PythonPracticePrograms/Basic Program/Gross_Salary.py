# 20. Write a program to input name and basic salary of an employee. Calculate and
# display the gross salary and net salary when :
# da = 30% of basic, hra = 12.5% of basic, pf = 10% of basic,
# gross= basic+ da+ hra,
# net pay = gross - pf

def getInput():
    basicSalary = int(input("Enter the Basic Salary of employee = "))
    return  basicSalary

def calculateGrossSalary(basicSalary,da=0.30,hra=0.125):
    return ((basicSalary*da) + (basicSalary*hra) +basicSalary)

def calculateNetSalary(basicSalary,grossSalary,pf=0.10):
    return (grossSalary - (basicSalary*pf))

basicSalary = getInput()
print("Basic Salary = ",basicSalary)
grossSalary = calculateGrossSalary(basicSalary)
print("Gross Salary = ",grossSalary)
netSalary = calculateNetSalary(basicSalary,grossSalary)
print("Net Salary = ",netSalary)