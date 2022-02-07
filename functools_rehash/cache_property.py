from functools import cached_property


class Employee(object):
    
    def __init__(self,eno,efirst,elast):
        self.eno =eno
        self.efirst =efirst
        self.elast =elast
    
    @property
    # @cached_property
    def email(self):
        print("Producing the Email from employee first and last name")
        return f"{self.efirst}.{self.elast}@email.com"
    
    @property
    # @cached_property
    def fullname(self):
        print("Producing the Fullname from employee first and last name")
        return f"{self.efirst} {self.elast}"
    
    @fullname.setter
    def fullname(self,fullname):
        first,last=fullname.split()
        self.efirst = first
        self.elast = last
    
    @fullname.deleter
    def fullname(self):
        self.efirst=None
        self.elast=None
        
        

emp1=Employee(eno=101,efirst="Abi",elast="Sarangi")
emp2=Employee(eno=102,efirst="Prarik",elast="Sarangi")

print(emp1.fullname)
print(emp2.email)
#this will be coming from the cached_property
print(emp1.fullname)
print(emp2.email)

emp1.fullname="Rika Sarangi"
print(emp1.efirst)
print(emp1.elast)

del emp1.fullname
print(emp1.efirst)
print(emp1.elast)

    
        