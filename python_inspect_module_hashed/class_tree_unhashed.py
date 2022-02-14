import inspect

class A(object):
    pass
class B(A):#inhertiting the class A
    pass
class C(A):#inhertiting the class A
    pass

child_tree=inspect.getclasstree([A,B,C])
# print(child_tree)
for item in child_tree:
    print(item)
    
# In [1]: from class_tree_unhashed import child_tree

# In [2]: child_tree[0]
# Out[2]: (object, ())

# In [3]: child_tree[1]
# Out[3]: 
# [(class_tree_unhashed.A, (object,)),
#  [(class_tree_unhashed.B, (class_tree_unhashed.A,)),
#   (class_tree_unhashed.C, (class_tree_unhashed.A,))]]

# In [4]: child_tree[1][0]
# Out[4]: (class_tree_unhashed.A, (object,))

# In [5]: child_tree[1][0][0]
# Out[5]: class_tree_unhashed.A

# In [6]: child_tree[1][1]
# Out[6]: 
# [(class_tree_unhashed.B, (class_tree_unhashed.A,)),
#  (class_tree_unhashed.C, (class_tree_unhashed.A,))]

# In [7]: child_tree[1][1][0]
# Out[7]: (class_tree_unhashed.B, (class_tree_unhashed.A,))

# In [8]: child_tree[1][1][1]
# Out[8]: (class_tree_unhashed.C, (class_tree_unhashed.A,))