print("asfkjhs")

a=9

def trying():
    #global a
    a=89
    x=globals()['a']
    print(id(x))
    globals()['a']=7487
    print("IN: ",a)

trying()
print("OUT ",a)
print(id(a))
