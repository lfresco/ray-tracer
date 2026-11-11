"""
Helper functions used throughout the application
"""

EPSILON = 0.00001

def equal(a:float, b: float) -> bool:
    """Compares two floating point numbers to see if they are close enough

    Args:
        a (float): float number
        b (float): float number

    Returns:
        bool: 
    """
    return abs(a - b) < EPSILON
        
    