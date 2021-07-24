# WAP to find given number is Harshad/Niven number or not
# An harshad number is an integer number divisible by sum of its digit
# Eg 18 sum=9 and 18 is divisible by 9

num = int(input("Enter the number = "))
numHold = num
sum=0
while(numHold>0):
    digit = numHold%10
    sum += digit
    numHold //= 10
print("sum=",sum)

if num%sum == 0:
    print(num," is Harshad Number")
else:
    print(num, " is not Harshad Number")