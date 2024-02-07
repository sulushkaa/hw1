import math
def Volume(radius):
    v = float((radius**3) * math.pi *(4/3))
    return v

rad = float(input("Enter your radius:"))
print(Volume(rad))