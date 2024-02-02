
class Room:
    def __init__(self, id_: str, name: str, description: str, exits_list: list, requires_key):
        self.id_ = id_
        self.name = name
        self.description = description
        self.exits_list = exits_list
        self.requires_key = requires_key
        self.exits = []

    def init_exits(self, exits: list):
        self.exits = exits


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.hp = 10
        self.current_room = current_room

    def input_handler(self, command):
        if "walk" in [cmd.lower() for cmd in command.split()]:
            pass

    def walk(self, new_room):
        self.current_room = new_room
        # if room_name in room_layout[self.position]:
        #     self.position = room_name
        # else:
        #     print('No such room')
        #     return False


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
