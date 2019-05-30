from item import Item
from player import Player
from room import Room
from textwrap import fill

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items=[Item('Sword', '''A dull-ish sword''')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('One', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def drop_or_get_item(cmd):
    global player

    cmd_split = cmd.split()
    action = cmd_split[0]
    item_name = ' '.join(cmd_split[1:])
    if action == 'drop':
        for item in player.inventory:
            if item.name.lower() == item_name:
                player.inventory.remove(item)
                return print(f'Item {item.name} dropped!')
        return print(f'No "{item_name}" in inventory')
    elif action == 'get':
        for item in player.current_room.items:
            if item.name.lower() == item_name:
                player.inventory.append(item)
                player.current_room.items.remove(item)
                return print(f'Item {item.name} added to inventory!')
        return print(f'No "{item_name}" in room')
    else:
        return print('Command not recognized')


def inventory():
    if player.inventory:
        print('Inventory:')
        for item in player.inventory:
            print(item.name, '\n', item.description)
        return print('----')
    else:
        return print('Inventory: No items!')


def move_room(cmd):
    global player
    if player.current_room[f'{cmd}_to']:
        player.current_room = player.current_room[f'{cmd}_to']
        return room_info()
    else:
        return print(f'Cannot move {cmd}')


def room_info():
    global player
    print('\n')
    print(f'Current Room: {player.current_room.name}')
    print(fill(player.current_room.description))
    if player.current_room.items:
        print('Items:')
        for item in player.current_room.items:
            print(item.name, '\n', item.description)
        return print('----')
    else:
        return print('Items: none')


# Initial display
room_info()

while True:
    print('\n')
    cmd = input('Enter Action: ').lower()
    # print(cmd)
    if cmd in ['n', 's', 'e', 'w']:
        move_room(cmd)
    elif 'drop' in cmd or 'get' in cmd:
        drop_or_get_item(cmd)
    elif cmd == 'inventory' or cmd == 'i':
        inventory()
    elif cmd == 'q':
        print('Thanks for playing!')
        break
    else:
        print('Command not recognized')
