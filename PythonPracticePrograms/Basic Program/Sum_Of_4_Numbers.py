# WAP to accept four digit number and do sum of digits

sum=0

for i in range(4):
    num = int(input("Enter the number = "))
    sum += num

print("Sum = ", sum)