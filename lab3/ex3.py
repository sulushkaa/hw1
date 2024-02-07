class Shape: 
    def area(self):
        return 0 
class Rectangle(Shape):
    def __init__(self, length, width ):
        self.length = float(length)
        self.width = float(width)
    def area(self):
     return self.length*self.width
    
rectangle_length = input ("Enter length of the rectangle:")
rectangle_width = input("Enter width of the rectangle:")
rectangle = Rectangle(rectangle_length, rectangle_width)
print("Area of the rectangle:", rectangle.area())