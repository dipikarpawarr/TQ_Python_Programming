# WAP program to count number of vowels in given string

lst = ['a','e','i','o','u']
count=0
strInput = input("Enter the string = ")

for i in strInput:
    for j in lst:
        if i==j:
            count += 1

print("Total vovels in a ", strInput, " are = ", count)