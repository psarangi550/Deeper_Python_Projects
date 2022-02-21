# class DictIter(object):
#     def __init__(self, dict_val):
#         self.dict_val = dict_val
#         self.val=0
#         self.current=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         list_keys=list(self.dict_val.keys())
#         if self.val<len(self.dict_val):
#             self.current=self.val
#             self.val=self.val+1
#             return list_keys[self.current]
#         raise StopIteration("Lets See")

# dict_iter=DictIter({"a":10,"b":20,"c":30,"d":40})

# for key in dict_iter:
#     print(key)
            

dict1={"a":10,"b":20}
print(list(dict1.items()))
# print(list(dict1.keys()))


# a=[10,20,30,40,10,20,50]
# a_set=set(a)
# print(a_set)
# print(dict.fromkeys(a))



