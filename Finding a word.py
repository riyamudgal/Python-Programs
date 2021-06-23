#reading text from a given file and finding a particular word
f=open("poem.txt","r")
t=f.read()
f.close()
a=t.find("twinkle")
print(a)
