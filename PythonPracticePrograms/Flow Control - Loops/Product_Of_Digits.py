# Write a Python program to calculate product of digits of any number.

num = int(input("Enter the number = "))
numHold = num
product = 1

while(numHold > 0):
    digit = numHold % 10
    product *= digit
    numHold //= 10

print("The product of the number ", num," is ", product)