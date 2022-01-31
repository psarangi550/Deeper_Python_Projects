
class Duck(object):
    def quack(self)->str:
        return "Quack Quack"
    def fly(self)->str:
        return "Flap fly"
class Human(object):
    def quack(self)->str:
        return "Human Trying to Quack"
    def fly(self)->str:
        return "Flaping the Arm in order to fly"

#Approaches non pythonic way
# def invoke_obj_methods(obj):
#     if not isinstance(obj,Duck):
#         return "The Object should be a Duck type to Quack"
#     return obj.quack()
#     return obj.fly()

# def invoke_obj_methods(obj):
#     if isinstance(obj,Duck):
#         if hasattr(obj,"quack") and hasattr(obj,"fly"):
#             if callable(obj.quack) and callable(obj.fly):
#                 return obj.quack(),obj.fly()
#             return "the provided method id not callable"
#         return "object does not have the property to  quack or fly"
#     return "object should be a duck type in order to quack or fly"


#pythonic approach:-
# def invoke_obj_methods(obj):
#     try:
#         quack=obj.quack()
#         fly=obj.fly()
#     except AttributeError as e:
#         print(e)
#     else:
#         return quack,fly

#
# duck1=Duck()
# print(invoke_obj_methods(duck1))
#
# human1=Human()
# print(invoke_obj_methods(human1))

###The Best Example will be  os.access() which will be in the gitpod example


