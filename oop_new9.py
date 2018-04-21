class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): #Repr is used to tell python how to represent something when the class is called
        return "(%d, %d, %d)" %(self.x, self.y, self.z) #This will display our numbers as (1, 2, 3) like points.

my_point = Point3D(1, 2, 3)

print my_point
