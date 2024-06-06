'''
import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)
'''
import logging
import os
from datetime import datetime
class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        
        #addition
        LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
        os.makedirs(log_path,exist_ok=True)

        LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
        ################################

        logging.basicConfig(filename=LOG_FILE_PATH,
                            filemode='w',
                            format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                            #format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m-%d-%Y %H:%M:%S')

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger