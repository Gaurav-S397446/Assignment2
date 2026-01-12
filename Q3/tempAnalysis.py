"""
temp_utils.py
This file contains all helper functions used for temperature analysis.
Only user-defined functions are used.
"""

import csv
import math
import os


def is_valid_number(value):
    """
    Checks if a value is a valid float number and not NaN.
    """
    try:
        num = float(value)
        return not math.isnan(num)
    except:
        return False
