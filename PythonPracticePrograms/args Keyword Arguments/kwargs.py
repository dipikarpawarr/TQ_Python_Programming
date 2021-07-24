def myFun(**kwInput):
    for key,value in kwInput.items():
        print("key=",key,"\tvalue=",value)

myFun(fname="Dipika", sname="Pawar", color="Royel Blue")