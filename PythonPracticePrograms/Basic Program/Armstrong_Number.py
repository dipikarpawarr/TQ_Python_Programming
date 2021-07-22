# WAP to check whether given number is three digit if yes check whether armstrong or not

number = int(input("Enter the number = "))

while number>0:
    number %= 10
    print(number)
