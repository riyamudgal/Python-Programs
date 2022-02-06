
#use open function to read the content of a file
f=open('dictionary.py','r')       #by default mode is r
data=f.read()
print(data)
f.close()               #after reading a file we must need to close it as well

#reading only first n characters of a file
f=open("fncode.py","r")
text=f.read(35)           #reads only first 35 characters of a file
print(text)
f.close()


#readline function
a=open("list.py","r")
text=a.readline()            #read the first line
print(text)
text=a.readline()             #reads first and second line both at the same time
print(text)
text=a.readline()              #reads the first three line at the same time
print(text)
text=a.readline()              #reads ths first four lines at the same time
print(text)
a.close()
