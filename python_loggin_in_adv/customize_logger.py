import logging

# logging.basicConfig(filename="test.log",level=logging.DEBUG,filemode="w",format="%(asctime)s:%(lineno)d:%(levelname)s:%(message)s")

logger=logging.getLogger(name=__file__)

logger.setLevel(logging.DEBUG)

# handler = logging.StreamHandler()

handler=logging.FileHandler(filename="custom.log",mode="w")

handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)

def test_add(a,b):
    return a+b

a=10
b=5

if __name__ == '__main__':
    logger.debug("addition of {} and {} is {}".format(a,b,test_add(a,b)))
    logger.info(" addition of {} and {} is {}".format(a,b,test_add(a,b)))




