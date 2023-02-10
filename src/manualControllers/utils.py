"""
Utility functions

By: s3a6m9
Version: 1.0
"""

def check_val(val):
    """ 
    Checks if val is between 0 and 1 so it can be used to send percentage 
    values to control the components.
    """
    if val < 0:
        return 0
    if val > 1:
        return 1
    return val
