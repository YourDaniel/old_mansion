
class Room:
    def __init__(self, name, exits):
        self.name = name
        self.exits = exits


class Player:
    def __init__(self, name, position):
        self.name = name
        self.hp = 10
        self.position = position

    def walk(self, room_name, room_layout):
        if room_name in room_layout[self.position]:
            self.position = room_name
        else:
            print('No such room')
            return False



class Inventory:
    items = []
    def __init__(self):
        pass

    def remove_item(self):
        pass
    def use_item(self):
        pass



class Item:
    def __init__(self, name):
        self.name = name
        self.description = ''