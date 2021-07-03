# write a program to generate multiplication tables from 2 to 20 and write it to the different files . place these files in a folder for a 13- year old student
for i in range(2,21):                                      #loop for number 
    with open(f"Tables/Table-of-{i}.txt","w") as a:        # opening a folder(files),Folder name-Tables, for each number different file will be created naming "Table-of-i.txt" in the folder
        for j in range(1,11):                              
            a.write(f"{i}*{j}={i*j}")                      #for printing table
            if(j!=10):                                     #for cursor to stop at 10
             a.write('\n')
