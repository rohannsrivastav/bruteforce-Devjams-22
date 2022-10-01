from datetime import datetime
now=datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

f = open("logs.txt", "w")

f.write(f"{dt_string}\n")


# entering the file names
firstfile = "master.txt"
secondfile = "new.txt"
    
# opening first file in append mode and second file in read mode
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r+')
 
# appending the contents of the second file to the first file
f1.write(f"{f2.read()}\n")
 
# relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)
 
f2.truncate(0)
# printing the contents of the files after appendng
# print(f1.read())
 
# closing the files
f1.close()
f2.close()