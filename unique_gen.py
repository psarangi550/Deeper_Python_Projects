import uuid
import time
# print(uuid.uuid1(clock_seq=None,node=14511))
#
# print(uuid.uuid1())
#
# print('mac address is ',uuid.getnode())
# print('mac is in hex code',hex(uuid.getnode()))

# UUID=uuid.uuid1() #creating the UUID class object
# print(UUID)
# print(type(UUID))
# print(UUID.version)
# print(UUID.variant)
# print(UUID)
# print(UUID.hex)
# print(UUID.int)
# print(UUID.time)
# print(UUID.time_low)
# print(UUID.time_mid)
# print(UUID.bytes_le)
# print(UUID.bytes)

#generating the same  UUID from the below o/p
# <class 'uuid.UUID'>
# b82bc6887c1511ec948bf47b09458390
# 244805246719874756477445588374086058896
# 138622121267676808
# 3089876616
# 31765
# b'\x88\xc6+\xb8\x15|\xec\x11\x94\x8b\xf4{\tE\x83\x90'
# b'\xb8+\xc6\x88|\x15\x11\xec\x94\x8b\xf4{\tE\x83\x90'

#here remember UUID is the class not the same as uuid.uuid1()
# UUID1=uuid.UUID(int=244805246719874756477445588374086058896)
# print(UUID1)
# UUID2=uuid.UUID(bytes_le=b'\xb8+\xc6\x88|\x15\x11\xec\x94\x8b\xf4{\tE\x83\x90')
# print(UUID2)
# UUID3=uuid.UUID(bytes=b'\x88\xc6+\xb8\x15|\xec\x11\x94\x8b\xf4{\tE\x83\x90')
# print(UUID3)


#converting thr uuid into string and reproducing the same uuid from the string
# UUID5=uuid.uuid1()
# print(UUID5)
# # print(UUID5.fields)#displaying all the field value in int format
# # str1=str(UUID5)
# str2=str(UUID5.hex)
# print("string value of uuid id ",str2)#convering the UUID class object into string type
# #regenrating the same UUID from the string
# UUID6=uuid.UUID(str2)
# print(UUID6)



#here also we can user UUID3 and UUID 5 which will be used with name and name spaces but the only difference is their hasing mechanism
#UUID3:-uses MD5 hasing
#UUID5 uses SHA-256 hashing

#name space has few properties on the UUID class objects
# UUID7=uuid.uuid3(uuid.NAMESPACE_DNS,'codewithpratik.com')
# print(UUID7)
# UUID8=uuid.uuid5(uuid.NAMESPACE_DNS,'codewithpratik.com')
# print(UUID8)

#1 observation :-
# The UUIDs generated at a different times using the same namespace and same name are equal.
# UUID7=uuid.uuid3(uuid.NAMESPACE_DNS,'codewithpratik.com')
# print(UUID7)
# time.sleep(10)
# UUID9=uuid.uuid3(uuid.NAMESPACE_DNS,'codewithpratik.com')
# print(UUID9)

#2nd observation
# The unique Ids generated from two different names in the same namespace are different.

# UUID7=uuid.uuid3(uuid.NAMESPACE_DNS,'codewithpratik.com')
# print(UUID7)
# UUID9=uuid.uuid3(uuid.NAMESPACE_DNS,'google.com')
# print(UUID9)

#3 observation:-

# The UUIDs generated from the same name in two different namespaces are different.

UUID7=uuid.uuid3(uuid.NAMESPACE_DNS,'codewithpratik.com')
print(UUID7)
UUID9=uuid.uuid5(uuid.NAMESPACE_DNS,'codewithpratik.com')
print(UUID9)