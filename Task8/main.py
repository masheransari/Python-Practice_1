from CircleClass import CircleClass
from RectangleClass import RectangleClass

r1 = RectangleClass(10.5, 2.5)

print("Area of rectangle r1:", r1.get_area())
r1.set_color("Blue")
print("Color of rectangle r1:", r1.get_color())

c1 = CircleClass(12)

print("\nArea of circle c1:", format(c1.get_area(), "0.2f"))
c1.set_color("Black")
print("Color of circle c1:", c1.get_color())