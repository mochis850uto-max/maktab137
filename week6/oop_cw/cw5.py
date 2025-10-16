class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2
    
r = Rectangle(18, 5)
print(f"rectangle area is", r.area())
print(f"rectangle perimeter is", r.perimeter())