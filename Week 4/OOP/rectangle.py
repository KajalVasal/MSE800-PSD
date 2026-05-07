class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.length * self.width
    
    def get_perimeter(self):
        return 2 * (self.length + self.width)
    
    def display_info(self):
        print(f"Rectangle: {self.length}m x {self.width}m")
        print(f"Area = {self.get_area()} sq meters")
        print(f"Perimeter = {self.get_perimeter()} meters")