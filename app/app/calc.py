"""
calculator functions
"""

def add(x, y):
    """Add x and y and return the result"""
    return x + y

def subtract(x, y):
    """Subtract x and y and return the absolute result"""
    res = x - y
    if res < 0:
        return -1 * res
    else:
        return res
