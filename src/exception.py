# This module defines a custom exception class and a function to generate detailed error messages.

import sys
from src.logger import logging

def error_message_details(error, error_detail: sys):
    '''
    Generate a detailed error message from an exception.
    '''

    _, _, exc_tb = error_detail.exc_info()
    error_message = f"Error occurred in python script: {exc_tb.tb_frame.f_code.co_filename}, line number: {exc_tb.tb_lineno}, error message: {str(error)}"
    
    return error_message

class CustomException(Exception):
    '''
    Custom exception class that extends the base Exception class.
    '''

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message