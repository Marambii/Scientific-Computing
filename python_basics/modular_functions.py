import math

def calculate_area(shape, dimension1, dimension2=0):
    if shape == "circle":
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return "Invalid shape"

# Test cases
print("Circle area (radius 5):", calculate_area("circle", 5))
print("Rectangle area (length 4, width 6):", calculate_area("rectangle", 4, 6))
print("Triangle area (base 3, height 7):", calculate_area("triangle", 3, 7))
print("Invalid shape:", calculate_area("hexagon", 3, 7))