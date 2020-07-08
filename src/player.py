# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def introduce_character(self):
        print(f'You hear a distant voice, "Open your eyes, {self.name}..."')

    def room_description(self):
        print(f'\nYou are at the {self.current_room.name}.\n{self.current_room.description}.')