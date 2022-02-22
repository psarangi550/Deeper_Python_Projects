import abc
# print(dir(abc))
class Student(abc.ABC):
    def __init__(self):
        pass
    @abc.abstractmethod
    def display(self):
        pass
    
class ChildStu(Student):
    def __init__(self):
        pass
    def display(self):#over riding the abstract method defined
        print("Hello")      

child_stu=ChildStu()

child_stu.display()