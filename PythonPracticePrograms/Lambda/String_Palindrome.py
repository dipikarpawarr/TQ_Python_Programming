# Write a Python program to find palindromes in a given list of strings using Lambda.

li=['abcd','xyzx','mom','deed','pqrstpu','dad']
print("\nlist = ", li)
print()
result = list(filter(lambda a: a==a[::-1],li))
print("Palindrome Strings = ",result)