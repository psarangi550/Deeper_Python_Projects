import json

class Employee(object):
    def __init__(self,name=None,salary=None):
        self.name = name
        self.salary = salary
    
    def display(self):
        return f"ENAME:-{self.name} ESAL:-{self.salary}"
    
    def __str__(self):
        return self.name
    
emp=Employee(name="pratik",salary=10000)
e_dict=emp.__dict__
# print(e_dict)
# print(type(e_dict))

#now serializing to json string
# print(json.dumps(e_dict))
# print(type(json.dumps(e_dict)))

#now serializing to a file

with open("emp.ser","w") as f:
    json.dump(e_dict,f)
    print("serialization happended successfully")
    
#now deserializing from json string to python object
# emp_obj_dict=json.loads(json.dumps(e_dict))
# emp=Employee(name=emp_obj_dict["name"],salary=emp_obj_dict["salary"])
# print(emp.display())

#now deserializing from the json file  to python object

with open("emp.ser","r") as f:
    e_dict=json.load(f)
    print(e_dict)
    emp=Employee(name=e_dict["name"],salary=e_dict["salary"])
    print(emp.display())

