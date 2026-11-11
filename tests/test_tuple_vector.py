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
    a = (4.3, -4.2, 3.1, 1)
    assert a[0] == 4.3
    assert a[1] == -4.2
    assert a[2] == 3.1
    assert is_point(a) is True
    assert is_vector(a) is False
    
def test_vector():
    """Test for the tuple representaton of a point"""
    a = (4.3, -4.2, 3.1, 0)
    assert a[0] == 4.3
    assert a[1] == -4.2
    assert a[2] == 3.1
    assert is_point(a) is False
    assert is_vector(a) is True