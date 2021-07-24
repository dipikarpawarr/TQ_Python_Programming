# WAP to check whether given number is special 2 digit number or not.
# A special two-digit number is a number such that when the sum of the digits of the
# number is added to the product of its digits, the result is equal to the original two-digit number.

# input: 29
# output: 29 is a Special Two-digit Number
# Explanation:
# Sum of digits = 9 + 2 = 11
# Product of digits = 9 * 2 = 18
# Sum of the sum of digits
# and product of digits = 11 + 18 = 29


number = int(input("Enter the number = "))
numHold = number
sum, product =0,1

while numHold>0:
    digit = numHold%10
    sum += digit
    product *= digit
    numHold //= 10

if number == (sum+product):
    print(number," is special number")
else:
    print(number, " is not special number")