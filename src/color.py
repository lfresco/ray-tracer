from src.tuples import Tuple

class Color(Tuple):
    
    def __init__(self, red: float, green: float, blue: float):
        self.red = red
        self.green = green
        self.blue = blue
    