#Program to demo variable pointing to which memoty address

# Number in between 0-255 wont create seperate object in memory but 256 and onwards create seperate object and stored in a heap memory. 
# when a=5 and b=5 at that time a and b pointing to same memory address.
# when a=500 and b=500, though values are same but it will create seperate object in heap memory. But this change you cannot seen in latest release.

a = 5
b = 5
print("a = ",a, "b = ", b)
print("Memory Address of a = ", id(a))
print("Memory Address of b = ", id(b))

a=500
b=500
print("\na = ",a, "b = ", b)
print("Memory Address of a = ", id(a))
print("Memory Address of b = ", id(b))