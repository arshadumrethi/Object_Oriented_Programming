class Animal(object):
    is_male = True
    def __init__(self, name, age, grass_eaten, is_hungry):
        self.name = name
        self.age = age
        self.grass_eaten = grass_eaten
        self.is_hungry = is_hungry

zebra = Animal("Jeffrey", 37, 450, True)

print "The zebras name is %s" %(zebra.name)
print "His age is %s" %(zebra.age)
print "Kilos of grass eaten is %s" %(zebra.grass_eaten)
print "Still Hungry? %s" %(zebra.is_hungry)
print "He is male %s" %(zebra.is_male)


# class Animal(object):
#   """Makes cute animals."""
#   is_alive = True
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# zebra = Animal("Jeffrey", 2)
# giraffe = Animal("Bruce", 1)
# panda = Animal("Chad", 7)
#
# print zebra.name, zebra.age, zebra.is_alive
# print giraffe.name, giraffe.age, giraffe.is_alive
# print panda.name, panda.age, panda.is_alive
