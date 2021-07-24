# WAP to accept 2 string and check whether they are anagram or not eg) MARY ARMY

strInput1 = input("Enter the first string = ")
strInput2 = input("Enter the second string = ")

if len(strInput1) == len(strInput2):
    sorted1 = sorted(strInput1)
    s1 = "".join(sorted1)

    sorted2=sorted(strInput2)
    s2 = "".join(sorted2)

    if s1 == s2:
        print("Anagram String")
    else:
        print("Not Anagram String")
else:
    print("Mismatch input")