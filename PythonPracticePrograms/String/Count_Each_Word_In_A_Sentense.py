# Write a Python program to count the occurrences of each word in a given sentence.

strInput = input("Enter the sentense = ")
lst = strInput.split(" ")

for i in lst:
    count = lst.count(i)
    print(i,"occurred ", count, " times.")