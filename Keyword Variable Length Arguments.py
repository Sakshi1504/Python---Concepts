def ran(name, *data):
    print(name)
    print(data)

ran("Sakshi", '23', 'gkt', 9897)

#want to show data specifically

def ran1(name, **data):
    print(name)
    print(data) #here it will print data in form of tuple
    #iterating in loop
    for i in data.items():
        print(i)
    print("------------------")
    for i,j in data.items():
        print(i,j)


ran1("Sakshii", Age='23', City='Gkt', Mob='8782')
