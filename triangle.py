import math

def herons_area(a, b, c):
    # Calculate half the perimeter
    s = (a + b + c) / 2
    
    # Calculate the area 
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# Enter input
side_a = float(input("length of side a: "))
side_b = float(input("length of side b: "))
side_c = float(input("length of side c: "))

triangle_area = herons_area(side_a, side_b, side_c)
print(f"The area of the triangle is: {triangle_area}")