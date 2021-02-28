list1=['a','b','c', 'c']
list2=['A','B','C', 'D']

zipped=list(zip(list1,list2))

print(zipped)

zipped=set(zip(list1,list2))

print(zipped)


zipped=tuple(zip(list1,list2))

print(zipped)

for (i,j) in zipped:
    print(i,j)



