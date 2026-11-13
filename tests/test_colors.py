from src.color import Color

def test_color_class():
    """Colors are (red, gree, blue) tuples
    """
    
    c : Color = Color(-0.5, 0.4, 1.7)
    assert c.red == -0.5
    assert c.green == 0.4
    assert c.blue == 1.7

def test_adding_colors():
    c1 : Color = Color(0.9, 0.6, 0.75)
    c2 : Color = Color(0.7, 0.1, 0.25)
    
    assert c1 + c2 == Color(1.6, 0.7, 1.0)

def test_subtracting_colors():
    """Scenario: Subtracting colors"""
    c1 : Color = Color(0.9, 0.6, 0.75)
    c2 : Color = Color(0.7, 0.1, 0.25)
    assert (c1 - c2) == Color(0.2, 0.5, 0.5)

def test_multiplication_by_scalar():
    """Scenario: Multiplying a color by a scalar"""
    
    c : Color = Color(0.2, 0.3, 0.4)
    assert c * 2.0 == Color(0.4, 0.6, 0.8)
    
def test_multiplication_colors():
    """Multiplying colors"""
    c1 : Color =  Color(1, 0.2, 0.4)
    c2 : Color = Color(0.9, 1, 0.1)
    assert c1 * c2 == Color(0.9, 0.2, 0.04)