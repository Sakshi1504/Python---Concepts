# import funcmodule then c=funcmodule.add(a,b) - this way it has to be done
#or
#from funcmodule import add
#or
#to import all functions
from funcmodule import *

#if we want to define all the function in other file, we'll have to import that module
a=5
b=10

c=add(a,b)

print(c)