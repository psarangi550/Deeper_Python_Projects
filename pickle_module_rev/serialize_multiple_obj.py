from multiple_object_to_file import main
import pickle
emp_list=main()
print(emp_list)
with open("emp.ser","wb") as f:
    pickle.dump(emp_list,f)
    print("serialization successful")