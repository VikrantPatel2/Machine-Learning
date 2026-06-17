import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result = a + b
    logger.debug("Adding %s + %s = %s", a, b, result)
    return result

def subtract(a, b):
    result = a - b
    logger.debug("Subtracting %s - %s = %s", a, b, result)
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug("Dividing %s / %s = %s", a, b, result)
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed.")
        return None

def multiply(a, b):
    result = a * b
    logger.debug("Multiplying %s * %s = %s", a, b, result)
    return result

add(10, 5)
subtract(10, 5)
divide(10, 0)
multiply(10, 5)