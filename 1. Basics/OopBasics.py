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