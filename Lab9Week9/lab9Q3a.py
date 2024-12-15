#Design a class to represent a rectangle. Some methods examples can
# be the rectangle area and rectangle perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length


    def info(self):
        print('The length of the rectangle is {}', self.length)
        print('The width of the rectangle is {}', self.width)


    def area(self):
        Area = self.width * self.length

        return '{} is the area of the rectangle'.format(Area)

    def perimeter(self):
        Perimeter = (self.width * 2 ) + (self.length * 2)

        return '{} is the perimeter of the rectangle'.format(Perimeter)


rectangle = Rectangle(4,3)
print(rectangle)
print(rectangle.area())
print(rectangle.perimeter())
rectangle.info