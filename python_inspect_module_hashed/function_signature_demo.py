import inspect
import requests

# sig=inspect.signature(requests.get)
# print(sig.parameters.values())
# print(type(sig))

#iterating over the signatire object
# for s in sig.parameters.values():
#     print(s)

#fetching kind over the iteration to fetch the kind
# for s in sig.parameters.values():
#     print(s.kind)


#getting the full argument signatiure using the getfullargspec function

print(inspect.getfullargspec(requests.get))
