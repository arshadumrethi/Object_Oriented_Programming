class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3

  number_of_sides = 3

  def check_angles(self):
    if self.angle1 + self.angle2 + self.angle3 == 180:
      return True
    else:
      return False

my_triangle = Triangle(90, 30, 60)

#Checking our methods and member variable
print my_triangle.number_of_sides
print my_triangle.check_angles()

##Creating a class called Equilateral that inherits from Triangle
class Equilateral(Triangle):
    angle = 60 #All angles of an equilater triangle are 60, hence we create this member variable
    def __init__(self):
        self.angle1 = self.angle #We assign each angle to our original member variable.
        self.angle2 = self.angle
        self.angle3 = self.angle
