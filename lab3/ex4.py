import math

class  Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def  show(self):
        return self.x, self.y
    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2+dy**2)
    
X = float(input("Enter x-coordinate:"))
Y = float(input("Enter y-coordinate:"))

point1 = Point(X, Y)
X = float(input("Enter another x-coordinate: "))
Y = float(input("Enter another y-coordinate: "))

point2 = Point(X, Y)

print("Coordinate of the first point", point1.show())
print("Coordinate of the second point", point2.show())

print("The distance between two points", point1.dist(point2))