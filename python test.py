def Calculate_Area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

result = Calculate_Area(length, width)

if type(result) == str:
    print(result)
else:
    print(f"The area of the rectangle is: {result}")

