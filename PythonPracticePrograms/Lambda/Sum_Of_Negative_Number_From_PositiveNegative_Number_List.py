# Write a Python program that removes the positive numbers from a given
# list of numbers. Sum the negative numbers and print the absolute value
# using lambda function.

li = [2,-2,-5,9,-1,4,-6,3,-7]
print("\nlist = ",li)
result = abs(sum(list(filter(lambda a : a<0,li))))
print("Sum = ", result)