from pyaml import yaml

emp_dict = {"ename":"rika","salary":100000}

################################################################
#converting the python dict into the yaml module
################################################################
# print(yaml.dump(emp_dict,indent=4,sort_keys=True))

################################################################
#deserailizing the yaml data to python dict using the safe_load() as load() been depricated 
################################################################
# e_dict=yaml.safe_load(yaml.dump(emp_dict,indent=4,sort_keys=True))
# print(e_dict)

################################################################
#converting the python dict to yaml string and write to a file using the dump()
################################################################ 
with open("emp.yaml","w") as f:
    yaml.dump(emp_dict,f,indent=4)
    print("serialization completed")
    
################################################################
#converting the file inside the yaml string and write to a file using the safe_load()
################################################################

with open("emp.yaml","r") as f:
    emp_dict=yaml.safe_load(f)
    print(emp_dict)