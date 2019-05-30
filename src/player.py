# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.current_room = current_room
        self.name = name
        self.inventory = inventory