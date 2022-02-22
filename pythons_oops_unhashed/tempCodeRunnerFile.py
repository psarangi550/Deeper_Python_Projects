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

child_stu=ChildStu()

child_stu.display()