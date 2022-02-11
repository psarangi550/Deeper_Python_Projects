import pickle

class Employee(object):
    def __init__(self,name=None,sal=None):
        self.name = name
        self.sal = sal
    
    def display(self):
        return f"ename is :-{self.name} salary is :- {self.sal}"

emp1=Employee(name='pratik',sal=1000)
with open("emp.ser","wb") as f:
    pickle.dump(emp1, f)
    print(" python object successfully saved to python file ")