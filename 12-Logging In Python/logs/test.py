from logger import logging

def add(a,b):
    logging.debug("Addition operation is taking place")
    return a+b
    
logging.debug("Addition operation is called")    
add(19,15)    