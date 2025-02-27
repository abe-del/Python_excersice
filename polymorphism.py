# the parent class
class shape:# it doesnot have attribute Q1
    def area(): # it is a void/placeholder/empty method[create to make the overriding purpose]
        pass#


# the first class that inherits from shape class Q2
class circle(shape):
    def __init__(self,radius):
        self.radius= radius #assigned the value of the radius parameter to the self.radius attribute
    # overrided the parent method
    def area(self):
        return 3.14* self.radius * self.radius


# the second sub class that inherits from the shape class Q2
class Rectangle(shape):
    def __init__(self,length,width): # the constructor class for the Rectangle method
        self.length= length # assigned the value of the length parameter to the self.length attribute
        self.width= width# assigned the value of the width parameter to the self.width attribute
    # overrided the parent method
    def area (self): # calculated the area of a rectangle
        return self.length*self.width


def calculate_area(shape):# it accepts objects as a parameter Q3
    return shape.area() # calling the area method/functipon that is found in the shape object


circle_object= circle(15) #Q4
rectangle_object=Rectangle(28,15)

print("-----------Circle Area-------")
print(calculate_area(circle_object)) # PASSED OBJECTS
print("----------Rectangle Area---------")
print(calculate_area(rectangle_object))

 
    