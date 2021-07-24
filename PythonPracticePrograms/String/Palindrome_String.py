# WAP program to check whether given string is palindrome

strInput = input("Enter the string = ")
strReverse = strInput[::-1]
if strInput==strReverse:
    print(strInput, " is palindrome string")
else:
    print(strInput, " is not palindrome string")