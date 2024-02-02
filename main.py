import json
from base_classes import Room, Player


def read_rooms_json():
    rooms_file = 'rooms.json'
    with open(rooms_file, 'r') as f:
        layout = json.load(f)
    return layout


def main():
    rooms_dict = read_rooms_json()
    ROOMS = {}
    for room_id in rooms_dict:
        ROOMS[room_id] = Room(
            room_id,
            rooms_dict[room_id]['name'],
            rooms_dict[room_id]['description'],
            rooms_dict[room_id]['exits'],
            rooms_dict[room_id].get('requires_key', False)
        )
    for room_id in ROOMS:
        exits = [ROOMS[exit_id] for exit_id in ROOMS[room_id].exits_list]
        ROOMS[room_id].init_exits(exits)

    print('ROOMS: ', end='')
    for room_id in ROOMS:
        print(ROOMS[room_id].id_, end=', ')
    print()

    player = Player('Daniel', ROOMS['car'])
    while True:
        print('Current position:', player.current_room.name)
        print('Rooms to go: ', end='')
        for room in player.current_room.exits:
            print(room.id_, end=' ')
        print()
        room_id = input('Where do you want to go? ')
        for room in player.current_room.exits:
            if room_id == room.id_:
                player.walk(room)


if __name__ == '__main__':
    main()



# TODO: map on the wall shows ASCII art of house plan
