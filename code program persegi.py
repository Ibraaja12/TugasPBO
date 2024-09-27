def calculate_rectangle_properties(length, width):
    # Calculate area
    area = length * width
    
    # Calculate perimeter
    perimeter = 2 * (length + width)
    
    return area, perimeter

# Input length and width of the rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Calculate and print area and perimeter
area, perimeter = calculate_rectangle_properties(length, width)
print("Area of the rectangle: ", area)
print("Perimeter of the rectangle: ", perimeter)