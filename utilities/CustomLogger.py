import logging
import inspect

def Custom_Logger(loglevel = logging.DEBUG):
    logname = inspect.stack()[1][3]
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(
        "C:\\Users\\indhu\\pythonlast\\pythonProject\\Amazon\\my_automation.log", mode='w')
    handler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s: %(name)s -  %(levelname)s: %(message)s',
                    datefmt='%m-%d-%Y %I:%M:%S %p')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger