class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self, age):
        print('Hello, my name is', self.name)
        print('Hello, my age is', self.age)

    # def my_age(self):
    #     print('Hello, my age is', self.age)


p = Person('Arshad')

a = Person('Ginger')

p.say_hi(14)
a.say_hi(12)
