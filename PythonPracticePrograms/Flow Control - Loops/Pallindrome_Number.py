# WAP to check given no is palindrome or not. Original =Reverse
# Eg 1221, 141, 12321, etc

num = input("Enter the number = ")
print("\n---- Solution 1 ----")
reverse = num[::-1]
if num == reverse:
    print(num," is palindrome")
else:
    print(num, " is not palindrome")

# OR

print("\n---- Solution 2 ----")

num1 = int(input("Enter the number = "))
numHold1 = num1
strReverse = ""
while(numHold1>0):
    digit = numHold1 % 10
    strReverse += str(digit)
    numHold1 //= 10
if num == strReverse:
    print(num," is palindrome")
else:
    print(num, " is not palindrome")