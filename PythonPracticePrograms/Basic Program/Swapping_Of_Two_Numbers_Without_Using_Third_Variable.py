# Write a program to demonstrate swappint of number without using third varible.

num1 = int(input("enter the value of num1 = "))
num2 = int(input("enter the value of num2 = "))

print("\n\nBefore swapping :- ")
print("num1 = ",num1)
print("num2 = ",num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("\nAfter swapping :- ")
print("num1 = ",num1)
print("num2 = ",num2)


#========================  in efficient way  ==============================================

num1, num2 = num1, num2


print("\nAfter swapping :- ")
print("num1 = ",num1)
print("num2 = ",num2)