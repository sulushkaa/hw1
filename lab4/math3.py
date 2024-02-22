import math

def polygon_area(n, s):
    return (1/4) * n * s**2 * (1 / math.tan(math.pi / n))

num_sides = int(input("Enter the number of sides of the polygon: "))
side_length = float(input("Enter the length of each side of the polygon: "))
print("Area of the regular polygon:", polygon_area(num_sides, side_length))