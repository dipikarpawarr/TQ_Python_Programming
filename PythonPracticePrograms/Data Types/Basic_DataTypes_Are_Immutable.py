# WAP to demonstrate basic datatypes are immutable (cant change the value.. always create new object
# after performin  updation on it)

# int is immutable
a=55
print("a=",a,"\tMemory Location",id(a))
a += 5
print("a=",a,"\tMemory Location",id(a))
b=60
print("b=",b,"\tMemory Location",id(b))
print()

# float is immutable
c=1.2
print("c=",c,"\tMemory Location",id(c))
d=5.8
print("d=",d,"\tMemory Location",id(d))
e=5.8
print("e=",e,"\tMemory Location",id(e))
print()

# str is immutable
s1='dipamraj'
print("s1=",s1,"\tMemory Location",id(s1))
s2='swapnil'
print("s2=",s2,"\tMemory Location",id(s2))
s3='swapnil'+'Patil'
print("s3=",s3,"\tMemory Location",id(s3))

a=8
b=4
print(a**b)