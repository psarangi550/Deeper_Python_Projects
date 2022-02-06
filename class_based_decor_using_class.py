
#defining  the decorator class which will correspond to the original class PrintName
class DecorPrintName(object):
    def __init__(self,cls):#definging the function name
        self.cls = cls
    def __call__(self, *args, **kwargs):
        my_class=self.cls(*args, **kwargs)
        for arg in kwargs:
            if kwargs[arg]=="Sarangi":
                original_name=my_class.print_name(arg)
                modified_name=f"Mrs {original_name}"
                return modified_name
            else:
                return self.func(*args, **kwargs)
        return my_class.print_name(*args,*kwargs)

@DecorPrintName
class PrintName(object):
    def __init__(self,name=None):
        pass
    def __str__(self):
        return self.name
    def print_name(self,title):
        return self.name+title

p1=PrintName("Rika")
print(p1)



