class Reservation:
    def __init__(self,guest_name): # the constructor method
        self.__guest_name= guest_name #private attribute
        self.__room_number= 101
# the method /function to assign a room for a specific guest
    def assign_room(self,room_number):
        self._room_number=room_number
## method to view the guest information
    def get_guest_info(self):#tries to display the guest name and room__number
        return f"Guest:{self.__guest_name},Room:{self.__room_number}"
reservation= Reservation("Alice Brown") # the 1st reservation is object while the 2nd is class    
reservation.assign_room(101)

print(reservation.get_guest_info()) #output: Guest: Alice Brown,Room:

        
    