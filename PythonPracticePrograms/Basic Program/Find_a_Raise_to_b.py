#Write a program to find a raise to b accept a and b from user

a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))

result=1

for i in range(b):
        result *= a
print("a raise to b = ", result)