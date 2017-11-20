import logging

def before_all(context):
    logging.basicConfig(level=logging.DEBUG, filename="./test.log")



