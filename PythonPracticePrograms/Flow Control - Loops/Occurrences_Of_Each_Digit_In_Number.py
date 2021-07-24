# Write a Python program to find frequency of each digit in a given integer.

num = int(input("Enter the number = "))

numHold1 = num
strHold = ""

while(numHold1 > 0):
    count = 0
    numHold2 = num
    digit1 = numHold1 % 10
    while numHold2 > 0:
        digit2 = numHold2 % 10
        if digit1 == digit2:
                count += 1
        numHold2 //= 10
    print(digit1, " is occurred ", count, " times.")
    numHold1 //= 10


