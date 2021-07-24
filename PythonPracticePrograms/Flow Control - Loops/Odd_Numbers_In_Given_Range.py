# WAP to print odd numbers from 521 to 229 using while loop.

def oddNumbers(sNumber, eNumber):
    while(sNumber >= eNumber):
        if sNumber%2!=0:
            print(sNumber)
            sNumber -=2

num1 = int(input("Enter the start number = "))
num2 = int(input("Enter the end number = "))
oddNumbers(num1,num2)