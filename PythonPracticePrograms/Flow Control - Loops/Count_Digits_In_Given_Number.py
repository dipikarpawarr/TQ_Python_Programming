# Write a Python program to count number of digits in any number

num = int(input("Enter the number = "))
numHold = num
count = 0
while(num>0):
    digit = num %10
    count += 1
    num //= 10
print("Total digits in the ",numHold," is = ", count)