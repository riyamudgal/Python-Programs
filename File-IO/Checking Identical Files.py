# write a program to find out whether a file is identical & matches the content of another file
file1="TextFile.txt"                           #storing first file name in file1 variable
file2="Copy.txt"                               #storing second file name in file2 variable

with open (file1) as f:                        #open file using file variable
    content1=f.read()                          #storing contents of file1 in content1

with open (file2) as f2:
    content2=f2.read()                         #storing contents of file2 in content2

if content1==content2:                         #comapring contents of two files
    print("Files are identical")
else:
    print("Files are not identical")
