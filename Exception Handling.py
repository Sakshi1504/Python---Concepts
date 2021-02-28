a=5
b=5


try:
    print(a/b)
    k=int(input("Enter any number: "))
    print(k)

except ZeroDivisionError:
    print("Zero Division error occured")

except ValueError as e:
    print(e)

except Exception as e:
    print("Can't divide by Zero. ", e)
finally:#finally gets executed no matter what
    print ("input some other value")