from src.color import Color
from src.canvas import Canvas

def all_black(c) -> bool:
    """Helper function that checks if the pixels
    have been correctly initiated to black

    Args:
        c (_type_): Canvas object

    Returns:
        bool: True if all pixels are black 
    """
    for row in range(c.height):
        for col in range(c.width):
            if c[row][col] == Color(0, 0, 0):
                continue
            return False
    return True

def test_canvas_init():
    
    c : Canvas = Canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    assert all_black(c) is True

def test_writing_on_cavas():
    """Writing pixels to canvas
    """
    canvas : Canvas = Canvas(10, 20)
    red : Color = Color(1, 0, 0)
    canvas[2][3] = red
    assert canvas[2][3] == red