from src.color import Color

class Canvas:
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.canvas = [[Color(0, 0, 0) for _ in range(width)] for _ in range(height)]   
        
    def __getitem__(self, key):
        return self.canvas[key]

    def __setitem__(self, key, value):
        self.canvas[key] = value