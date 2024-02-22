def parallelogram_area(base, height):
    return base * height

base_length = float(input("Enter the base length of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))
print("Area of the parallelogram:", parallelogram_area(base_length, height))