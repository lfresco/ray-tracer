from src.color import Color

def test_color_class():
    """Colors are (red, gree, blue) tuples
    """
    
    c : Color = Color(-0.5, 0.4, 1.7)
    assert c.red == -0.5
    assert c.green == 0.4
    assert c.blue == 1.7
    