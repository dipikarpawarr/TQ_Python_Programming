# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

list1 = ["a","dipa","def","diya","priya","dipali","dipshikha"]
print(list1)

count = 0

for i in list1:
    if len(i) >= 2:
        for j in list1:
            ilen = len(i)-1
            jlen = len(j)-1
            if i!=j and i[0]==j[0] and i[ilen]==j[jlen]:
               #print(i)
			   count += 1
               break
print("Total Strings are : ",count)