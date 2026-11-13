from typing import Union
from src.helpers import equal

class Color:
    
    def __init__(self, red: float, green: float, blue: float):
        self.red = red
        self.green = green
        self.blue = blue
    
    def __add__(self, other: Color) -> Color:
        return Color(
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue
        )
    
    def to_tuple(self) -> tuple:
        """Converts Color to a tuple object

        Returns:
            tuple: tuple repr of colors
        """
        return (self.red, self.green, self.blue)
    
    def __eq__(self, other: Color) -> bool:
        return equal(self.red, other.red) and equal(self.green, other.green) and equal(self.blue, other.blue)

    def __sub__(self, other: Color) -> Color:
        return Color(
                    self.red - other.red,
                    self.green - other.green,
                    self.blue - other.blue
                )
    
    def __mul__(self, other: Union[Color, float]) -> Color:
        if isinstance(other, float):
            return Color(
                self.red * other,
                self.green * other,
                self.blue * other
            )
        if isinstance(other, Color):
            return Color(
                self.red * other.red,
                self.green * other.green,
                self.blue * other.blue
            )