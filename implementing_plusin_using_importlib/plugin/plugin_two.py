class Plugin(object):#definging the class object which can take any no of arguments while instanciating

    def __init__(self,*args,**kwargs):#definging the constructor function
        print("initialization completed for plugin_two with %s " % kwargs)#this will be published once the object instanciated

    def execute(self,a,b):#instance method
        return a-b #returning the additional value

