import math

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def perimeter(self):
        return (2 * self.width) + (2 * self.length)
    def area(self):
        return self.width * self.length

class Square:
    def __init__(self, length):
        self.length = length
    def perimeter(self):
        return 4 * self.length
    def area(self):
        return self.length**2

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius**2

print("Hi! Which of the following shapes would like to calculate the area or perimeter? ")
print("Choose one of the following options:")
print("Rectangle")
print("Square")
print("Circle")

user = input("\n> ")
user = user.lower()
user = user.strip()

match user:
    case "rectangle":
        choice = input("Would like to calculate area or perimeter of the rectangle? ")
        w = float(input("Enter a width of the rectangle: "))
        l = float(input("Enter a length of the rectangle: "))
        r = Rectangle(w, l)
        match choice:
            case "perimeter":
                print(f"The perimeter of the rectangle is: {round(r.perimeter(), 2)}")
            case "area":
                print(f"The area of the rectangle is: {round(r.area(), 2)}")

    case "square":
        pass


