import sys
from src.logger import logging

def error_message_detais(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name[{0}] line number[{1}] error message[{2}]".format()
    file_name, exc_tb.tb_lineno, str(error)

    return error_message
def CustomException(xception):
    def__init__(self, error_message, error_detail:sys):
    super().__init__(error_message)
    self.error_message = error_message_detail(error_message. error_details = error_details)

def__str__(self):
    reeturn self.error_message


if __name__=="__main__":
    try:
        a =1/0
    except Exception as e:
        logging.info("Divided by zero")
        rasie CustomException(e,sys)

