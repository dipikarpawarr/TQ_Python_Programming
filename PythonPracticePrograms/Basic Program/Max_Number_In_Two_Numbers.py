# Write a program to accept 2 number and find greatest

def maxNumber(number1, number2):
    if num1 > num2:
        print("\nMax number is ", number1)
    else:
        print("\nMax number is ", number2)

num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))

maxNumber(num1,num2)

# OR

print("\n\n----- Max number is = ", max(num1,num2))

