from functools import lru_cache

import time

#lru cache stands for least recently used
#that means the least recently used cache will be replaced by the  new cache once the cache maxsize is reached
#here using the lru cached with max size which is default to 128
# @lru_cache
# def sleep_time(sec):
#     # print("printing before going into sleep")
#     time.sleep(sec)
#lru cache with max_size mentioned in lru_cache
#@lru_cache(maxsize=2,typed=True)#:-case-2
@lru_cache(maxsize=3,typed=True)#:-case-3
def sleep_time(sec):
    # print("printing before going into sleep")
    time.sleep(sec)

#case:-1
# if __name__ == "__main__":
#     print("printing before going into sleep")
#     sleep_time(4)
#     print("sleeping again.....")
#     sleep_time(4)#expecting thie to be cached and execute faster
#     print("sleeping cycle completed")
    
#case:-2
if __name__ == "__main__":
    print("printing before going into sleep")
    sleep_time(4)
    print("sleeping again.....")
    sleep_time(1)
    print("sleeping again.....")
    sleep_time(2)
    print("sleeping again.....")
    sleep_time(4)
    print("sleeping cycle completed")