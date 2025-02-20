class Hotel:# Iam defining a class
    def __init__(self,name,numberOfRooms,location,services):#are parameters to be passedwhile creating an object
        self.name = name # is an attribute to hold the name data
        self.numberOfRooms = numberOfRooms # is an attribute to hold number of rooms
        self.location = location # is an attribute to  hold location
        self.services = services # is an attribute to hold services
    # to create a Read Operation function
    def viewHotelRooms(self):
        return f"The hotel {self.name} has {self.numberOfRooms} rooms"
    def viewHotelLocation(self):
        return f"The hotel {self.name} is in {self.location}"
    def viewHotelservices(self):
        return f"The hotel {self.name} has a  {self.services}"
    
    
# creating an object based on the class
object_1 = Hotel("Eliana",150,"Addis Ababa","swimming pool,spa,meeting hall")
object_2 = Hotel("Sheraton",1500,"Addis Ababa","Spa, meeting hall")
print(object_1.viewHotelRooms())
object_3 = Hotel("Hilton",2500,"Addis Ababa","Spa, meeting hall")
print(object_3.viewHotelLocation(),object_3.viewHotelservices())

    