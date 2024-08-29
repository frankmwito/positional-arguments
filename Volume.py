# calculate the volume of a rectangular prism

def volume(length, width, height):
    return length * width * height
# calculate the volume of a rectangular prism

length = float(input("Enter the length:"))
width = float(input("Enter the width:"))
height = float(input("Enter the height:"))

result = volume(length, width, height)

print("The volume is:", result)
