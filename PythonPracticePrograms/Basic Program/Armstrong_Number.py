# WAP to check whether given number is three digit if yes check whether armstrong or not

number = int(input("Enter the number = "))

numHold = number
sum = 0
while numHold>0:
    digit = numHold % 10
    sum += digit ** 3
    numHold //= 10

if sum == number:
    print(number , " is armstrong number")
else:
    print(number , " is not armstrong number")


