import logging
from customize_logger import *

def test_add(a,b):
    return a+b

a=10
b=5

logger.debug("addition of {} and {} is {}".format(a,b,test_add(a,b)))
logger.info(" addition of {} and {} is {}".format(a,b,test_add(a,b)))