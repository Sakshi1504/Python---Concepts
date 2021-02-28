import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)

i=0
def hi():
    global i
    i+=1
    print("Han han mai crazy hu.",i)
    #hi()

hi()

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))