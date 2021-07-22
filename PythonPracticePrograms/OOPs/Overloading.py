class Overloading_Demo:
    # Keyword argument
    def add(self, a=0,b=0,c=0):
        return a+b+c

    def add(self, w=3,x=5,y=7,z=9):
        return w+x+y+z

obj = Overloading_Demo()
print(obj.add(3,6))
print(obj.add(11,5,12))