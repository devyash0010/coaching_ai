'''   Utility functions that are used across the analytics folder.  '''


def calculate_percentage(obtained_marks, total_marks):

    if total_marks == 0:
        return 0
    else:
        return round((obtained_marks / total_marks) * 100, 2)  # this round function stores till two decimal values.


def safe_divide(a, b):  # why use this == because what if 10/0 --> our file will crash so for safety purpose.

    if b == 0:
        return 0
    else:
        return round(a / b, 2)