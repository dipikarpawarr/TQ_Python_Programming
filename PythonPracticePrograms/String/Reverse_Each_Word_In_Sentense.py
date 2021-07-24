# WAP to reverse each word in a sentence Python is fun -->nohtyP si nuf

strInput = input("Enter the a sentense = ")

lst = strInput.split(" ")
for strHold in lst:
    reverse = strHold[::-1]
    print(reverse, end=" ")