from multiple_object_to_file import *
import pickle
with open("emp.ser","rb") as f:
    while True:
        try:
            emp_list=pickle.load(f)
        except EOFError:
            break
        except TypeError:
            print(emp_list.display())
            break
        else:
            for emp in emp_list:
                print(emp.display())
        
        
        
                
    