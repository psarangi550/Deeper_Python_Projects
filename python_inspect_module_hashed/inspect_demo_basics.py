import inspect
import requests
resp=requests.get("https://httpbin.org/ip")
print(resp.status_code)
print(resp.text)


'''
    This files reference to inspect module 
    which will help in inspect all the class or objects or function or module 
    this will return the addition of 2 values
'''

def test_add(a,b):
    '''
    This files reference to inspect module 
    which will help in inspect all the class or objects or function or module 
    this will return the addition of 2 values
    '''
    return a + b

###getting the response code property using the inspect module getmembers function
# print(inspect.getmembers(resp))

####get the response from the requests.Request class using the inspect module getsource() function
# print(inspect.getsource(requests.Request))
#using the grsourcelines() as an alternate to getsource() function which will provide the list in response
# print(inspect.getsourcelines(requests.Request))

##fetching the docs using inspect.getdoc() function
# print(inspect.getdoc(test_add))

###fetching the file reference using the getfile()
print(inspect.getfile(test_add))
print(inspect.getfile(requests.get))
