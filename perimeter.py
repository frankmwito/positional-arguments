# perimeter of a quadrilateral

def perimeter(length, width):
    
    return  2 * (length + width)
length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

result = perimeter(length, width)

print("The perimeter of a quadrilateral is:", result)