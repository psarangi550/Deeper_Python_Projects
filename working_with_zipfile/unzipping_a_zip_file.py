import zipfile
import inspect
# zip=zipfile.ZipFile("all_file.zip","w",zipfile.ZIP_DEFLATED)

# zip.write("f1.txt")
# zip.write("f2.txt")
# zip.write("f3.txt")

# print("Done")

unzip=zipfile.ZipFile("all_file.zip","r",compression=zipfile.ZIP_STORED)

# print(list(unzip))

# print(dir(unzip))

print(unzip.namelist())

for file in unzip.namelist():
    with open(file,"r") as f: 
        print(f.read())
        print()
# print(inspect.getfullargspec(zipfile.ZipFile))
# for file in unzip:
#     print(file.read())