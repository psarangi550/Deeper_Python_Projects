import logging

# logging.basicConfig(filename="test.log",level=logging.DEBUG,filemode="w",format="%(levelname)s:%(name)s:%(message)s")
logging.basicConfig(filename="test.log",level=logging.DEBUG,filemode="w",format="%(asctime)s:%(lineno)d:%(levelname)s:%(message)s")
def test_add(a,b):
    return a + b

a=10
b=5

logging.info("addition of {} and {} is {}".format(a,b,test_add(a,b)))

    