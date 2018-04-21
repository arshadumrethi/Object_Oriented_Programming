class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg

  def display_car(self):
    print "This is a %s, %s with %s MPG" %(self.color, self.model, str(self.mpg))

  def drive_car(self):
      self.condition = "used"

#Electric Car is a child class of Car and inherits its methods
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg = mpg
    self.battery_type = battery_type

  def drive_car(self): #Over riding the drive_car method of the Parent Class by creating our own method here
      self.condition = True

my_car = ElectricCar("Tesla", "silver", 89, "molten salt")

#my_car = Car("DeLorean", "silver", 88)
# print my_car.model
# print my_car.color
# print my_car.mpg
# print my_car.display_car()

print my_car.condition
my_car.drive_car()
print my_car.condition
