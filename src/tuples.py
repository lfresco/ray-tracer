"""
This module contains the tuple implementation of the point and the vector
"""
def point(x: float, y: float, z: float) -> tuple:
    """Returns a tuple representation of the point 

    Args:
        x (float): the x coordinate
        y (float): y coordinate
        z (float): z coordinate

    Returns:
        tuple: point representation with w = 1
    """
    return(x, y, z, 1)

def vector(x: float, y: float, z: float) -> tuple:
    """Returns a tuple representation of the vector 
    
        Args:
            x (float): x coordinate
            y (float): y coordinate
            z (float): z coordinate
    
        Returns:
            tuple: vector representation with w = 0
        """
    return(x, y, z, 0)

class Tuple:
    """Tuple base element
    """
    def __init__(self, x: float, y: float, z: float, w: float):
        """Initialize a Tuple element
        
            Args:
                x (float): x coordinate
                y (float): y coordinate
                z (float): z coordinate
                w (float): 1 for point, 0 for vector
            """
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def to_tuple(self) -> tuple:
        """Returns the tuple representation of the Tuple class

        Returns:
            tuple: _description_
        """
        return (self.x,self.y,self.z,self.w,)
    
    def __add__(self, other):
        return Tuple(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w
        )
    
    def __sub__(self, other):
        return Tuple(
                    self.x - other.x,
                    self.y - other.y,
                    self.z - other.z,
                    self.w - other.w
                )
    
    def __neg__(self):
        """Negation of a Tuple

        Returns:
            Tuple: returns a Tuple with negated elements
        """
        return Tuple(
            -self.x,
            -self.y,
            -self.z,
            -self.w
        )
        

class Point(Tuple):
    """Class representinf the point tuple
    """
    def __init__(self, x: float, y: float, z: float):
        """Initialize a Tuple element with w = 0

            Args:
                x (float): x coordinate
                y (float): y coordinate
                z (float): z coordinate
            """
        self.t = Tuple(x, y, z, 1.0)
    
    def to_tuple(self) -> tuple:
        """Returns tuple representation of the Point object

        Returns:
            tuple: tuple with coordinates
        """
        return self.t.to_tuple()

    def __add__(self, other) -> Tuple:
        """Operator overload for the addition

        Args:
            other (_type_): object that has a tuple 

        Returns:
            _type_: _description_
        """
        return self.t.__add__(other.t)

    def __sub__(self, other):
        """Operator overload for the subtraction

        Args:
            other (_type_): object that has a tuple 

        Returns:
            _type_: _description_
        """
        return self.t.__sub__(other.t)
    
    def __neg__(self):
        
        return self.t.__neg__()
class Vector(Tuple):
    """Class representation of the Vector
    """
    def __init__(self, x: float, y: float, z: float):
        """Initialize a Tuple element with w = 0

        Args:
            x (float): x coordinate
            y (float): y coordinate
            z (float): z coordinate
        """
        self.t = Tuple(x, y, z, 0.0)
    
    def to_tuple(self) -> tuple:
        """Returns tuple representation of the Point object
        
        Returns:
            tuple: tuple with coordinates
        """
        return self.t.to_tuple()
    
    def __add__(self, other):
        """Operator overload for the addition

        Args:
            other (_type_): object that has a tuple 

        Returns:
            _type_: _description_
        """
        return self.t.__add__(other.t)

    def __sub__(self, other):
        """Operator overload for the subtraction

        Args:
            other (_type_): object that has a tuple 

        Returns:
            _type_: _description_
        """
        return self.t.__sub__(other.t)
    
    def __neg__(self):
            return self.t.__neg__()