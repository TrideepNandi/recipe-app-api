"""
calculator functions
"""


def add(x, y):
    """add x and y and return the result"""


    return x + y
def subtract(x, y):
    """subtract x and y and return the result"""


    res = x - y
    if res < 0:
        return -1*res
    else:
        return res
