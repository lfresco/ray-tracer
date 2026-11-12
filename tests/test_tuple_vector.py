from src.tuples import Vector, Point, Tuple

def is_point(a: tuple) -> bool:
    """This function verify if givn tuple is a point based on the
        assumption that if the last element of the tuple is a q than
        we are dealing with a point
    
        Args:
            a (tuple): tuple composed of 4 elements, the last of which
                        tells if it is a vector or a point
    
        Returns:
            bool: 
        """
    return a[-1] == 1

def is_vector(a: tuple) -> bool:
    """This function verify if givn tuple is a vector based on the
    assumption that if the last element of the tuple is a 0 than
    we are dealing with a vector

    Args:
        a (tuple): tuple composed of 4 elements, the last of which
                    tells if it is a vector or a point

    Returns:
        bool: 
    """
    return a[-1] == 0
 
def test_point():
    """Test for the tuple representation of a point"""
    a : tuple = (4.3, -4.2, 3.1, 1)
    assert a[0] == 4.3
    assert a[1] == -4.2
    assert a[2] == 3.1
    assert is_point(a) is True
    assert is_vector(a) is False
    
def test_vector():
    """Test for the tuple representaton of a point"""
    a : tuple = (4.3, -4.2, 3.1, 0)
    assert a[0] == 4.3
    assert a[1] == -4.2
    assert a[2] == 3.1
    assert is_point(a) is False
    assert is_vector(a) is True
    
def test_point_fun():
    """Testing the point function
    """
    p : Point = Point(4, -4, 3)
    assert p.to_tuple() == (4, -4, 3, 1)

def test_vector_fun():
    """Testing the vector function
    """
    v : Vector = Vector(4, -4, 3)
    assert v.to_tuple() == (4, -4, 3, 0)

def test_addiction():
    """Test for the addition operations
    """
    a1 : Point = Point(3, -2, 5)
    a2 : Vector = Vector(-2, 3, 1)
    assert (a1 + a2).to_tuple() == (1, 1, 6, 1)
    
def test_subtraction():
    """Test for the subtraction operation
    """
    p1 = Point(3, 2, 1)
    p2 = Point(5, 6, 7)
    assert (p1 - p2).to_tuple() == Vector(-2 , -4, -6).to_tuple()

def test_subtracting_vec_from_point():
    """Subtracting a vector from a point
    """
    p = Point(3, 2, 1)
    v = Vector(5, 6, 7)
    assert (p - v).to_tuple() == Point(-2, -4, -6).to_tuple()

def test_subtracting_two_vectors():
    """The subtraction of two vectors gives us a Vector
    """
    v1: Vector =  Vector(3, 2, 1)
    v2: Vector = Vector(5, 6, 7)
    assert (v1 - v2).to_tuple() == Vector(-2, -4, -6).to_tuple()
    
def test_negation():
    """Negating a tuple
    """
    a: Tuple = Tuple(1, -2, -3, 4)
    assert (-a).to_tuple() == Tuple(-1, 2, 3, -4).to_tuple()
    
def test_multiplying_scalar():
    """Multiplying a tuple for a scalar
    """
    a : Tuple = Tuple(1, -2, 3, -4)
    assert (a * 3.5).to_tuple() == Tuple(3.5, -7, 10.5, -14).to_tuple()

def test_multiplying_by_fraction():
    """Multiplying fractions
    """
    a : Tuple = Tuple(1, -2, 3, -4)
    assert (a * 0.5).to_tuple() == Tuple(0.5, -1, 1.5, -2).to_tuple()

def test_dividing():
    """Dividing by a scalar
    """
    a : Tuple = Tuple(1, -2, 3, -4)
    assert (a / 2).to_tuple() == Tuple(0.5, -1, 1.5, -2).to_tuple()

def test_magnitude():
    """Scenario: Computing the magnitude of vector(1, 0, 0)
    """

    v : Vector = Vector(1, 0, 0)
    assert v.magnitude() == 1.0