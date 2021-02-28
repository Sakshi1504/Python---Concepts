#jsdkf
from functools import reduce
list1=[4,54,32,2,66,7,5,9]

evens=list(filter(lambda x: x%2==0,list1))

print(evens)
#map takes every value and performs operation on it.
doubles = list(map(lambda a: a+2, evens))

print(doubles)

#reduce the values - here want to add the values
#reduce belongs to function tool module
sum=reduce(lambda a,b: a+b,doubles)

print(sum)
