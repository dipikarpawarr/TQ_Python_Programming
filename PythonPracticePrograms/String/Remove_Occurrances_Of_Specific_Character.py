# WAP to remove all occurences of given char from String

strInput = input("\nEnter the string = ")
charRemove = input("Which character you have to remove = ")

result = strInput.replace(charRemove,"")
print("\nBefore = ", strInput)
print("After = ",result)