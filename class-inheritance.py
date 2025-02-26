#Basic/ parent /super class
class Hotel:
    def __init__(self,name,location):
    #this class has two attributes;name and location
       self.name= name
       self.location=location
    #Method for read operation{it reads/display the name and the location}
    def hotelDescription(self):
        return f"The hotel{self.name}is located in{self.location} area"
 #the child class
class LuxuryHotel(Hotel):
    def __init__(self,name,location,VIPservices):#the constructor method of the child
        super().__init__(name,location)# the constructor method of the parent class
        self.VIPservices = VIPservices #the attribute of the child class
    def hotelDescription(self):
        print("The Luxury hotel",self.name,"is located in",self.location,"area and provides",self.VIPservices,"services")
              
my_luxury_hotel__object = LuxuryHotel("Sheraton","Addis Ababa","swimming pool")
print(my_luxury_hotel__object.hotelDescription())