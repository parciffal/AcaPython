class Hotel:
    def __init__(self, name: str, city: str, rooms: dict={}):
        self.__city = city
        self.__rooms = rooms
        self.__name = name

    def rooms_str(self):
        return "".join(["\n{}: {}".format(k, self.rooms[k]) for k in self.rooms.keys()])

    def __repr__(self):
        return "City: {}\nName: {}\nRooms: {}"\
               .format(self.city, self.name, self.rooms_str())

    def free_room_list(self, room_type):
        if room_type in self.rooms.keys():
            return self.rooms[room_type]
        else:
            return None

    def reserve_room(self, room_type: str, room_count):
        if room_type not in self.rooms.keys():
            return False
        else:
            if self.rooms[room_type] < room_count:
                print("We don't have so much rooms : {}".format(self.rooms[room_type]))
                return False
            else:
                self.rooms[room_type] -= room_count
                return True

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, room: dict):
        self.__rooms = room

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
