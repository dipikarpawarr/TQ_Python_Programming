# Write a Python program to find sum of all even numbers between 1 to n.

num = int(input("Enter the number = "))
sum=0
for i in range(1,num+1):
    if i%2==0:
        sum += i
print("The sum = ", sum)