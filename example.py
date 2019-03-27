import logging
from logging.config import fileConfig
from json_logging import JSONExtras 

fileConfig('logging_config.ini')
logger = logging.getLogger()

def exampleFunction():
    logger.debug("Woo", extra=JSONExtras({'type': 'x', 'version': '1.1'}))
    logger.info("Woo", extra=JSONExtras({'type': 'x', 'version': '1.1'}))
    logger.warning("Woo", extra=JSONExtras({'type': 'x', 'version': '1.1'}))
    logger.error("Woo", extra=JSONExtras({'type': 'x', 'version': '1.1'}))
    logger.critical("Woo", extra=JSONExtras({'type': 'x', 'version': '1.1'}))
    
if __name__ == "__main__": 
    exampleFunction()
