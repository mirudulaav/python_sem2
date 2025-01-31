class HotelRoom:
    def __init__(self, room_num, rate_per_night):
        self.__room_num= room_num
        self.__is_occupied = False
        self.__rate_per_night = rate_per_night

    def get_room_number(self):
        return self.__room_num
    def set_room_number(self, room_num):
        if room_num> 0:
            self.__room_num= room_num
  
    def get_rate_per_night(self):
        return self.__rate_per_night
    def set_rate_per_night(self, rate_per_night):
        if rate_per_night > 0:
            self.__rate_per_night = rate_per_night
        else:
            raise ValueError("Rate per night must be greater than zero.")

    def check_in(self):
        if self.__is_occupied:
            raise Exception("The room is already occupied.")
        self.__is_occupied = True
    def check_out(self):
        if not self.__is_occupied:
            raise Exception("The room is already vacant.")
        self.__is_occupied = False

    def display_details(self):
        print(f"Room Number: {self.__room_num}")
        print(f"Rate per Night: ${self.__rate_per_night:.2f}")
        print(f"Occupied: {'Occupied' if self.__is_occupied else 'Vacant'}")

room = HotelRoom(101, 200.50)
room.display_details()

    
