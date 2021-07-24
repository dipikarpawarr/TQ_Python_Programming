# WAP to check given no is Krishnamurthy or not
# eg) 145=1!+4!+5!=145 ===> (1)+(4*3*2*1)+(5*4*3*2*1)=145

num = int(input("Enter the number = "))
numHold = num
sum=0
while (numHold > 0):
    digit = numHold % 10
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    numHold //= 10
    sum += fact

if num == sum:
    print(num," is Krishnamurthy Number")
else:
    print(num, " is not Krishnamurthy Number")