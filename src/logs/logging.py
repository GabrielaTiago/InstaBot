import logging

def logging_config():
    logging.basicConfig(filename='src/logs/logs.log', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def info(msg):
    logging.info(msg)

def warning(msg):
    logging.warning(msg)

def error(msg):
    logging.error(msg)

def debug(msg):
    logging.debug(msg)

def critical(msg):
    logging.critical(msg)

def exception(msg):
    logging.exception(msg)
