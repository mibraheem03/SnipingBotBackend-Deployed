import logging
from datetime import datetime

formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s')
from logging.handlers import QueueHandler
log = logging.getLogger('log')
log.setLevel(logging.DEBUG)
logFileName = datetime.now().strftime('Log/log_%H_%M_%d_%m_%Y.log')
mainLogFile_handler = logging.handlers.RotatingFileHandler(logFileName, mode='a', maxBytes=52428800, backupCount=5,
                                                           encoding=None, delay=False, errors=None)
mainLogFile_handler.setFormatter(formatter)
log.addHandler(mainLogFile_handler)
