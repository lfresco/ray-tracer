"""
This module contains the tuple implementation of the point and the vector
"""
from math import sqrt

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
    
    def __mul__(self, other: Tuple) -> Tuple:
        return Tuple(
            self.x * other,
            self.y * other,
            self.z * other,
            self.w * other
        )
    
    def __truediv__(self, other: Tuple) -> Tuple:
        return Tuple(
            self.x / other,
            self.y / other,
            self.z / other,
            self.w / other
        )
    
    def __eq__(self, other: Tuple) -> bool:
        return self.to_tuple() == other.to_tuple()

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
        super().__init__(x=x, y=y, z=z, w=1.0)
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
        super().__init__(x = x, y = y, z = z, w = 0.0)
    
    def magnitude(self) -> float:
        """Computes magnitude of a vector

        Returns:
            _type_: _description_
        """
        return sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w))
    
    def normalize(self) -> Vector:
        """Transform the Vector into the unit vector

        Returns:
            Vector: unit vector
        """
        magnitude = self.magnitude()
        
        return Vector(
            x = self.x / magnitude,
            y = self.y / magnitude,
            z = self.z / magnitude)
    
    def dot(self, other: Vector):
        """Compute the dot product of the vector
        with another one

        The smaller the product, the larger the angle
        betweem the vectors
        Args:
            other (Vector): another vector

        Returns:
            _type_: _description_
        """
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z +
            self.w * other.w
        )
    
    def cross(self, other: Vector) -> Vector:
        """Cros product

        Args:
            other (Vector): another vector

        Returns:
            Vector: the resulting vector
        """
        return Vector(
            x= self.y * other.z - self.z * other.y,
            y = self.z * other.x - self.x * other.z,
            z = self.x * other.y - self.y * other.x
        )