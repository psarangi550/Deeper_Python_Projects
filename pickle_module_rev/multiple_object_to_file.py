import pickle
emp_list=[]
class Employee(object):
    def __init__(self,name=None,sal=None):
        self.name = name
        self.sal = sal
    
    def display(self):
        return f"ENAME:-{self.name} SAL:{self.sal}"
    
    def __str__(self):
        return self.name

def main():
    while True:
        name=input("Enter your name")
        sal=int(input("Enter your Salary"))
        emp=Employee(name=name, sal=sal)
        emp_list.append(emp)
        option=input("Do you wish to add one more record [y/n]:")
        if option.lower() == 'n':
            print("thanks for using the application")
            break
    return emp_list


# if __name__ == '__main__':
#     emp_list_details=main()
#     print(emp_list_details)
        
        
        
            
            