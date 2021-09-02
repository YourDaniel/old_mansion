import json
from base_classes import Room, Player


def read_rooms_json():
    rooms_file = 'rooms.json'
    with open(rooms_file, 'r') as f:
        layout = json.load(f)
    return layout


ROOMS_LAYOUT = read_rooms_json()


def main():

    ROOMS = []
    for room in ROOMS_LAYOUT.keys():
        ROOMS.append(Room(room, ROOMS_LAYOUT[room]))
    player = Player('Daniel', ROOMS[0].name)
    while True:
        print('Current position:', player.position)
        print('Rooms to go:', ROOMS_LAYOUT[player.position])
        read_key = int(input('Where to go? (1,2,3,4...)'))
        target_room_name = ROOMS_LAYOUT[player.position][read_key-1]
        player.walk(target_room_name, ROOMS_LAYOUT)





if __name__ == '__main__':
    main()
