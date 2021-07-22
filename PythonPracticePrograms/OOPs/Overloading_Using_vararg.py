import functools


class Overloading2:
    def add(*num):
        add=0
        for i in num:
            add += i
        #print(functools.reduce(lambda a,b: a+b,num)
        #print(filter((lambda a, b: a + b), num)
    print(add)

obj = Overloading2()
obj.add(21,22,10,10)