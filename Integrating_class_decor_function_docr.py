def decor1(func):#defining the decorator method
    def wrapper(*args, **kwargs):
        for arg in kwargs:
            if kwargs[arg]=="Sarangi":
                return f"{func(*args, **kwargs)} Good Afternoon"
            else:
                return func(*args, **kwargs)
    return wrapper


class PrintName(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    @decor1
    def print_name(self,title):
        return str(self.name)+title

p1=PrintName("Rika")
print(p1.print_name(title="Sarangi"))