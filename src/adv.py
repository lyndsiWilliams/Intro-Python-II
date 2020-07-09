from room import Room
from player import Player
from item import Item


# Declare all the items

item = {
    'sword': Item("Sword", "Made of iron with a sturdy hilt wrapped in leather."),

    'shield': Item("Shield", "Made of iron with sturdy leather straps."),

    'ring': Item("Ring", "One to rule them all."),

    'bag': Item("Bag", "Can hold a surprising amount of items.")
}

# Declare all the rooms and put items inside

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['bag']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['sword'], item['shield']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['ring']]),
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


def the_game():
    # New character
    player = Player("Lyndsi", room['outside'])

    # "Playing" boolean to turn the game on/off, turned on
    playing = True

    # Game introduction
    player.introduce_character()

    # Prompt player for input
    def input_prompt():
        selection = input("\nWhat will you do next?\n"
                          "Press [c] for controls.\n\n")
        # Await player selection
        input_response(selection)

    # Room movement
    def move_to(selection):
        denial = "\nYou skid to a stop as you can go no further. Try moving in a direction with an entrance."

        # North
        if selection == "n":
            # if n_to path exists on current room...
            try:
                # Send player to the room to the north
                player.current_room = player.current_room.n_to
            except:
                print(denial)
                # Prompt player for input
                input_prompt()
        # South
        elif selection == "s":
            # if s_to path exists on current room...
            try:
                # Send player to the room to the south
                player.current_room = player.current_room.s_to
            except:
                print(denial)
                # Prompt player for input
                input_prompt()
        # East
        elif selection == "e":
            # if e_to path exists on current room...
            try:
                # Send player to the room to the east
                player.current_room = player.current_room.e_to
            except:
                print(denial)
                # Prompt player for input
                input_prompt()
        # West
        elif selection == "w":
            # if w_to path exists on current room...
            try:
                # Send player to the room to the west
                player.current_room = player.current_room.w_to
            except:
                print(denial)
                # Prompt player for input
                input_prompt()
        # Invalid input
        else:
            print("\nThat is not a valid selection.")
            input_prompt()

    # Player input response

    def input_response(selection):
        if len(selection) == 1:
            # Controls list
            if selection == "c":
                print("\nControls: \n"
                      " - Observe your surroundings [o]\n"
                      " - Look through your items [i]\n"
                      " - Search for items in the area [f]\n"
                      " - Get an item [get item_name]\n"
                      " - Drop an item [drop item_name]\n"
                      " - Walk to another room [n, s, e, w]\n"
                      " - Stop playing [q]")
                # Prompt player for input
                input_prompt()

            # Observe room
            elif selection == "o":
                # Current room description
                player.room_description()
                # Prompt player for input
                input_prompt()

            # Player items
            elif selection == "i":
                print("\nYou search through your belongings:")
                # If the player has any items
                if player.items:
                    # Loop through items
                    for i in player.items:
                        print(f" - {i}")
                else:
                    print("\n - You have no items.")
                # Prompt player for input
                input_prompt()

            # Inspect for items in room
            elif selection == "f":
                print('\nYou inspect the area for items and see...\n')
                if player.current_room.items:
                    player.current_room.room_items()
                else:
                    print('There are no items in the area.')

            # Get an item
            elif selection == "get":
                if item:
                    # Add item to player's belongings
                    player.items.append(item)
                    # Remove item from room
                    player.current_room.items.remove(item)
                    # "Item get" message
                    item.item_get()
                else:
                    print("That item is not in this room.")
                # Prompt player for input
                input_prompt()

            # Drop an item
            elif selection == "drop":
                if item:
                    # Remove item to player's belongings
                    player.items.remove(item)
                    # Add item back into the room
                    player.current_room.items.append(item)
                else:
                    print("You do not have that item.")
                # Prompt player for input
                input_prompt()

            # Directional movement
            elif selection in ("n", "s", "e", "w"):
                move_to(selection)

            # Stop playing
            elif selection == "q":
                print("\nThank you for playing! See you next time!")
                nonlocal playing
                playing = False

            # Invalid input
            else:
                print("\nThat is not a valid selection.")
                input_prompt()

    while playing:
        # Current room description
        player.room_description()

        # Prompt player for input
        input_prompt()


# Initiate gameplay
the_game()
