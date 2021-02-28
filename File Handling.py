f1 = open('Exception Handling.py', 'r')

print(f1)

##print(f1.read()) #prints all the data of the file
print(f1.readline(2))  # it will print only two characters of the file

f1.close()

f = open('abc', 'a')
f.write("Hi")
f2=open('abc', 'r')

for data in f2:
    #print(data, end="")
    f.write(data)  #copying data from one file to other

#image files are binary files, contains numbers n all
img=open('download ps.jpg', 'rb')

print(img.read())

imgwr=open('please.JPG', 'wb')



for i in img:
    imgwr.write(i)
