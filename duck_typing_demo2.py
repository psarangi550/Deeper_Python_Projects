import os

from isort import file 

#python _documentation explore
#non pythonic way:-LBYL:-look before you leave

file_name="data.txt"

# if os.access(file_name,os.R_OK):
#     with open(file_name, "r") as f:
#         data=f.read()
#         print(data)
# else:
#     print("file is not readable")

if os.access(file_name,os.W_OK):
    with open(file_name, "a+") as f:
        f.write("Good Morning\n")
        print(f.read())
else:
    print("file is not writeable")

##to change it back to read mode -->use chmod 400 data.txt
###to change it to the write mode-->use chmod 700 data.txt


###chenging the permission as--> chmod 000 data.txt 

