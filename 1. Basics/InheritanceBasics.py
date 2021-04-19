# Syntax:

# class parent:
#       statements
# class child(parent):
#       statements


class Quadrilateral:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        p = self.a + self.b + self.c + self.d
        print("perimeter: ", p)


q1 = Quadrilateral(4, 5, 7, 9)
q1.perimeter()


class Rectangle(Quadrilateral):
    def __init__(self, a, b):
        super(Rectangle, self).__init__(a, b, b, a)

    def area(self):
        area = self.a * self.b
        print("Area:", area)


r1 = Rectangle(20, 10)
r1.perimeter()
r1.area()


class Square(Rectangle):
    def __init__(self, a):
        super(Square, self).__init__(a, a)

    def area(self):     # overRiding
        area = pow(self.a, 2)
        print("AREA: ", area)


print("Square...")
s1 = Square(9)
s1.perimeter()
s1.area()
