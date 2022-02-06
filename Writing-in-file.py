#writing files in python
f=open("css.txt","w")
f.write("It is also an another coding language that is used along with HTML.")
f.close()

#appending(adding) the data at the end
f=open("css.txt","a")
f.write(" CSS stands for Cascading Style Sheet")
f.close()
