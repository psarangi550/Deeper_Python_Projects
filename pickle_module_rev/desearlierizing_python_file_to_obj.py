import pickle
from serialized_pickle import Employee
with open("emp.ser","rb") as f:#opening it in the read mode
    e1=pickle.load(f)
    print(type(e1))
    print(e1.display())#calling the instance method 

    