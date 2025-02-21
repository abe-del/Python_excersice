class Hotel:
    def __init__(self,name,location,rooms):
        """Initialize thehotel with a name,location,and number of rooms"""
        self.name = name #hotel name
        self.location = location # hotel location
        self.rooms = rooms # total number of rooms
        self.booked_rooms = 0 # rooms currently booked
     # book info create operation
    def book_room(self, number_of_rooms):
        #"""Book a specified number of rooms"""
        if number_of_rooms <=0:
            print("Number of rooms to book must be positive.")
            return
        if self.booked_rooms + number_of_rooms> self.rooms: #room-means
            print("Not enough available rooms to book.")
            return
        self.booked_rooms +=number_of_rooms
        print(f"{number_of_rooms}room(s) successfully booked.")
        #book info delete operation
    def checkout(self,number_of_rooms):
            #"""check out a specfied number of rooms."""
        if number_of_rooms<= 0:
            print("Number of rooms to check out must be positive.")
            return
        if number_of_rooms > self.booked_rooms:
            print("can not check out more rooms than booked.")
            return
        self.booked_rooms -= number_of_rooms
        print(f"{number_of_rooms} room(s)) successfully checked out.")
    def get_availability(self):
        """Get the number of available rooms."""
        available_rooms = self.rooms -self.booked_rooms
        return available_rooms
    def __str__(self):

        """ Return a string representation of the hotel."""
        return f"Hotel:{self.name},location:{self.location},Totalrooms:{self.rooms},booked rooms:{self.booked_rooms}"


# Creating an object of the hotel class
my_hotel = Hotel("Seaside Resort","California", 40)
# Accessing attributes and methods
print(my_hotel) # Display hotel details
# Booking rooms
my_hotel.book_room(22)
print(f"Available rooms: {my_hotel.get_availability()}") #check available rooms
# checking out rooms
my_hotel.checkout(4)
print(f"Available rooms:{my_hotel.get_availability()}") #check available rooms    

