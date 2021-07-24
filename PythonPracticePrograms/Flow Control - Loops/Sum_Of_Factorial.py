# 1!+2!+3!.........+n! find sum

num = int(input("Enter the number = "))
sum = 0
for i in range(1, num+1):
    fact = 1
    for j in range(1,i+1):
        fact *= j
    sum += fact
print("sum=",sum)