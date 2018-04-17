class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print "Hippo's name is %s" %(self.name)
    print "Hippo's age is %s" %(self.age)

hippo = Animal("Anderson", 36)
hippo.description()
