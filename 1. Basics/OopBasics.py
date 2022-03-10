'''
            Python Object Oriented Concepts Include:
1. Classes - objects, instance, attribute, method
2. Inheritance
3. Polimophism
4. Abstraction
5.
'''
# like functions classes also allow you to compartmentalize code and data. object stems from the fact that
# the model resembles objects in the real word in that each object is a thing that has certain attributes and 
# characteristics that make it unique.

# Class 
# A piece of code from which you can generate a unique object, where each object is a single instance of 
# the class. Think of it as a blueprint or factory from which you can create individual objects.
class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def display_name(self):
        print(self.name)

    def display_age(self):
        print(self.age)

# Instance 
# One unit of data plus code generated from a class as an instance of that class. 
# Each instance of a class is also called an object created by class.
puppy = Dog(3, 'TOM')
bull_dog = Dog(5, 'Bravo')

# Attribute: A characteristic of an object that contains information about the object. 
# Also called a property of the object. An attribute name is preceded by dot, as in member.username 
# which may contain the username for one site member.
puppy.age
puppy.name 

# Method: A Python function that’s associated with the class. It defines an action that object can perform. 
# In an object, you call a method by preceding the method name with a dot, and following it with a pair of parentheses. 
# For example member.archive() may be a method that archives (deactivates) the member’s account.
puppy.display_age()
puppy.display_name()
puppy.change_name("Cindy")
puppy.display_name()


class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def display_name(self):
        print(self.name)

    def display_age(self):
        print(self.age)


puppy = Dog(3, 'TOM')
puppy.display_age()
puppy.display_name()
puppy.change_name("Cindy")
puppy.display_name()



'''
                Inheritance
'''
# inheritance is by creating sub-classes within a class. The class defines things that apply to all instances of 
# that class. Each subclass defines things that are relevant only to the subclass without replacing anything 
# that’s coming from the generic “parent” class.

# Syntax:

class parent:
   statements
class child(parent):
   statements

# Subclasses inherit all the attributes and methods of some higher-level main class, or 
# parent class, which is usually referred to as the base class.

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


