class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is: ", self.side**2)
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("My area is: ", 3.14*self.radius*self.radius)

osquare = Square(3)
ocircle = circle(3)

for shape in(osquare, ocircle):
    shape.area()