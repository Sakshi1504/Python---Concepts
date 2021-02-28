#as string/int

x=input("Enter anything")
print("hi, I'm : ",x, " and I'm a : ", type(x))


x=int(input("Enter anything"))
print("hi, I'm : ",x, " and I'm a : ", type(x))


x=input("Enter anything")[1]
print("hi, I'm : ",x, " and I'm a : ", type(x))

#taking command line arguments-
import sys

a=int(sys.argv[1])
b=int(sys.argv[2])
print(a+b)