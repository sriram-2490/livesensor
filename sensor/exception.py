import sys
import os 

def get_error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in filename is [{0}] at line number [{1}] error message is [{2}]".format(
        filename, exc_tb.tb_lineno, str(error))
    return error_message

class SensorException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.errormessage = get_error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.errormessage  # Changed from self.error_message to self.errormessage