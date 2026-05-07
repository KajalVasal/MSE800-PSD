from rectangle import Rectangle

try:
    length = float(input("Enter length in meters: "))
    width = float(input("Enter width in meters: "))
    
    land = Rectangle(length, width)
    land.display_info()
    
except ValueError as e:
    print("Error:", e)