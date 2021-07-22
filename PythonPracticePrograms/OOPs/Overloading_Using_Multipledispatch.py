from multipledispatch import dispatch

class Overloading1:
    @dispatch(int,int)
    def add(self,a,b):
        return (a+b)

    @dispatch(int, float, int)
    def add(self,i,f,j):
        return (i+f+j)

obj = Overloading1()

print(obj.add(3,4))
print(obj.add(3,4.5,5))