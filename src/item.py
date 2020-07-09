class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def item_description(self):
        print(f'{self.description}')

    def item_get(self):
        print(f'You add one (1) {self.name} to your belongings.')

    def item_drop(self):
        print(f'You carefully place the {self.name} on the ground.')
