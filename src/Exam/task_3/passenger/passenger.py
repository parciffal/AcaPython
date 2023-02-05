from Exam.task_3.hotel.hotel import Hotel


class WeDontHaveThatRoom(Exception):
    def __init__(self, count):
        super().__init__("We don't have {} type of rooms".format(count))


class Passenger:
    def __init__(self, name: str, city: str, rooms: dict = {}):
        self.__name = name
        self.__city = city
        self.__rooms = rooms

    def rooms_str(self):
        return "".join(["\n{}: {}".format(k, self.rooms[k]) for k in self.rooms.keys()])

    def __repr__(self):
        return "Name: {}\nCity: {}\nRooms: \n{}\n".format(self.name, self.city, self.rooms_str())

    def add_room(self, room_type: str, room_count=1):
        if room_type in self.rooms.keys():
            self.rooms[room_type] += room_count
        else:
            self.rooms[room_type] = room_count

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


def book_room(usr: Passenger, hotel: Hotel, room_type: str, room_count: int):
    if hotel.book_room(room_type, room_count):
        usr.add_room(room_type, room_count)
    else:
        raise WeDontHaveThatRoom(room_type)
