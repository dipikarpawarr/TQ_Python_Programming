# Write a program to demonstrate greater number from 3 values

num1 = int(input("Enter the num1 = "))
num2 = int(input("Enter the num2 = "))
num3 = int(input("Enter the num3 = "))

print("\n\nnum1 = ", num1, "  num2 = ",num2, "  num3 = ",num3)

if (num1 >= num2) and (num1 >= num3):
   print("\nGreater number is = ",num1)
elif (num2 >= num1) and (num2 >= num3):
   print("\nGreater number is = ",num2)
else:
   print("\nGreater number is = ",num3)