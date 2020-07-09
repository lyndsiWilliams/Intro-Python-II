# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def room_items(self):
        for i in self.items:
            print(f' - {i.name}: {i.description}')
