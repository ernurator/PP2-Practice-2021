class Dog:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age
    def bark(self):
        print('Gav')
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

d = Dog('Tuzik')
d2 = Dog('GGGG', 10)
d.bark()

print(d.get_name(), d.get_age())
print(d2.get_name(), d2.get_age())
