class Employee(object):
    def __init__(self,first,last):
        self.first = first
        self.last = last
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self,value):
        self.first=value.split()[0]
        self.last=value.split()[1]

    @fullname.deleter
    def fullname(self):
        self.first=None
        self.last=None




emp1=Employee("rika","sarangi")
print(emp1.fullname)
emp1.fullname="abi sarangi"
print(emp1.first)
print(emp1.email)
del(emp1.fullname)
print(emp1.first)
print(emp1.last)

