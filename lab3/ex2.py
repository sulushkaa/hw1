class Shape: 
    def area(self):
        return 0 
    
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return float(self.length)**2

square_length = input("Enter the length of the square:")
square = Square(square_length)
print("Area of the square:", square.area())
shape = Shape()
print("Area of the shape:", shape.area())