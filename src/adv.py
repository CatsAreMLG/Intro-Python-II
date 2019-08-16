import os
from room import Room
from player import Player
from item import Item

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

room['foyer'].add_item(Item('sword', 'I can schlice things with this.'))
room['foyer'].add_item(Item('helmet', 'This will protect my head.'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Travler')
player.set_room(room['outside'])

commands = {
    'take': 'You took ',
    'get': 'You took ',
    'drop': 'You dropped ',
    'n': 'You move north.',
    'e': 'You move east.',
    's': 'You move south.',
    'w': 'You move west.',
    'q': 'Are you sure you want to quit (Y/N)? '
}


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def print_invalid():
    print('+------------------+')
    print('|' + 'Invalid input.'.center(18, ' ') + '|')
    print('|' + 'get/take [item]'.center(18, ' ') + '|')
    print('|' + 'drop [item]'.center(18, ' ') + '|')
    print('|' + 'n - Move North'.center(18, ' ') + '|')
    print('|' + 's - Move South'.center(18, ' ') + '|')
    print('|' + 'e - Move East'.center(18, ' ') + '|')
    print('|' + 'w - Move West'.center(18, ' ') + '|')
    print('|' + 'q - Exit game'.center(18, ' ') + '|')
    print('+------------------+')
    return True


def validate_move(user_input):
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    actions = user_input.strip().split()
    if not actions:
        print_invalid()
        return True
    if actions[0] in commands:
        if len(actions) == 1:
            if actions[0] == 'q':
                yn = input(commands[actions[0]])
                clear()
                return yn.lower() == 'n'
            else:
                move_check = player.move(actions[0])
                if move_check:
                    return True
                else:
                    print('You can\'t go in that direction.')
                    print('--------------------------------')
                    return True
        elif len(actions) == 2:
            drop_check = take_check = False
            if actions[0] == 'take' or actions[0] == 'get':
                take_check = player.take_item(actions[1])
            elif actions[0] == 'drop':
                drop_check = player.drop_item(actions[1])
            if take_check or drop_check:
                return True
            else:
                print(f'There is no item with that name to {actions[0]}')
                print('--------------------------------')
                return True
        else:
            print_invalid()
            return True
    else:
        print_invalid()
        return True


# * Clear console
clear()
# Write a loop that:
while True:
    print(player.get_room())
    # * Waits for user input and decides what to do.
    #
    user_input = input('What will you do? ')
    # * Clear console
    clear()
    checked = validate_move(user_input)
    if not checked:
        break
    else:
        continue
