from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import sys


if __name__=="__main__":
    logging.info("Starting the application")
    logging.info("Application is running")
    logging.info("Application has finished execution")


    try:
        a=1/0
    except Exception as e:
        logging.info("custom Exception occurred")
        raise CustomException(e, sys)