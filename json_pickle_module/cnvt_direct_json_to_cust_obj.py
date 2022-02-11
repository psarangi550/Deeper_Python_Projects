import jsonpickle

class Employee(object):
    def __init__(self,name=None,salary=None):
        self.name = name
        self.salary = salary
    
    def display(self):
        return f"ENAME:-{self.name} ESAL:-{self.salary}"
    
    def __str__(self):
        return self.name

emp=Employee(name="Pratik",salary=2000)
################################
#converting custom python object to json directly using the json pickle module 
################################
# print(jsonpickle.encode(emp))

################################################################
#converting the json data to python object directly using json pickle module decode()
################################################################

# json_string=jsonpickle.encode(emp)
# emp=jsonpickle.decode(json_string)
# print(emp)
# print(type(emp))
# print(emp.display()) 

################################################################
#converting the python object to json string and saved it to a file using the file i/o operation
################################################################
json_string=jsonpickle.encode(emp,indent=4)
with open("emp.ser","w") as f:
    f.write(json_string)
    print("serialization to the file successfully completed")

################################################################
#converting the saved json file to python object and calling the display instance method on it 
################################################################

with open("emp.ser","r") as f:
    json_string=f.read()
    emp_obj=jsonpickle.decode(json_string)
    print(emp_obj.display())
    

     
