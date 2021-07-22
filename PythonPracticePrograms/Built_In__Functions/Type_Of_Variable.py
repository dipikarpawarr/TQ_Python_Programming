#input() takes any number or string or float or character as a string
holdVariable = int(input("Enter whole number : "))
print("\nInput : ", holdVariable)
print("Type of ",holdVariable, "is :", type(holdVariable))

holdVariable = float(input("\nEnter float number : "))
print("Input : ", holdVariable)
print("Type of ",holdVariable, "is :", type(holdVariable))

holdVariable = str(input("\nEnter string : "))
print("Input : ", holdVariable)
print("Type of ",holdVariable, "is :", type(holdVariable))

holdVariable = bool("True")
print("\nInput : ", holdVariable)
print("Type of ",holdVariable, "is :", type(holdVariable))
