from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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
                          "Press [c] for controls.")
        # Await player selection
        input_response(selection)

    # Room movement
    def move_to(selection):
        denial = "\nYou run into a wall... Try moving in a direction with an entrance."

        # North
        if selection == "n":
            # if n_to path exists on current room...
            if player.current_room.n_to:
                # Send player to the room to the north
                player.current_room = player.current_room.n_to
            else:
                print(denial)
                # Prompt player for input
                input_prompt()
        # South
        elif selection == "s":
            # if s_to path exists on current room...
            if player.current_room.s_to:
                # Send player to the room to the south
                player.current_room = player.current_room.s_to
            else:
                print(denial)
                # Prompt player for input
                input_prompt()
        # East
        elif selection == "e":
            # if e_to path exists on current room...
            if player.current_room.e_to:
                # Send player to the room to the east
                player.current_room = player.current_room.e_to
            else:
                print(denial)
                # Prompt player for input
                input_prompt()
        # West
        elif selection == "w":
            # if w_to path exists on current room...
            if player.current_room.w_to:
                # Send player to the room to the west
                player.current_room = player.current_room.w_to
            else:
                print(denial)
                # Prompt player for input
                input_prompt()

    # Player input response
    def input_response(selection):
        if len(selection) == 1:
            # Controls list
            if selection == "c":
                print("\nControls: \n"
                      " - Observe your surroundings [o]\n"
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
