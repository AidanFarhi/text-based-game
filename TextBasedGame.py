# Aidan Farhi - 2023-06-13


def get_command() -> tuple:
    """Prompts the user to enter a command and returns it as a tuple.

    Returns:
        tuple: A tuple containing the command and its arguments.
    """
    command = input("Enter Command > ")
    command = tuple(command.split())
    return command


def validate_item_command(command: tuple, current_room: dict) -> bool:
    if current_room['item'] is None or command[1:] != tuple(current_room['item'].split()):
        print(f'Cannot get {command[1]}')
        return False
    return True


def validate_move_command(command: tuple, current_room: dict) -> bool:
    """Validates a move command.

    Args:
        command (tuple): A tuple containing the command and its arguments.
        current_room (dict): A dictionary representing the current room and its connections.

    Returns:
        bool: True if the move command is valid, False otherwise.
    """
    direction = command[1]
    if direction not in ("north", "east", "west", "south"):
        print("Direction must be: <north|east|west|south>.")
        return False
    elif direction not in current_room:
        print("You cannot go that direction!")
        return False
    return True


def validate_command(command: tuple, current_room: dict) -> bool:
    """Validates a command.

    Args:
        command (tuple): A tuple containing the command and its arguments.
        current_room (dict): A dictionary representing the current room and its connections.

    Returns:
        bool: True if the command is valid, False otherwise.
    """
    valiation_result = True
    if len(command) > 3:
        print("Invalid input!")
        valiation_result = False
    elif command[0] not in ("go", "get"):
        print("Invalid input!")
        valiation_result = False
    elif command[0] == "go":
        valiation_result = validate_move_command(command, current_room)
    elif command[0] == 'get':
        valiation_result = validate_item_command(command, current_room)
    return valiation_result


def handle_direction_command(command: tuple, current_room: dict) -> str:
    """Handles a direction command.

    Args:
        command (tuple): A tuple containing the command and its arguments.
        current_room (dict): A dictionary representing the current room and its connections.

    Returns:
        str: The new room after moving in the specified direction.
    """
    direction = command[1]
    new_room_name = current_room[direction]
    return new_room_name


def handle_item_command(current_room: dict, inventory: list) -> None:
    """Handles an item command.
    
    Args:
        current_room (dict): A dictionary representing the current room and its connections.
        inventory (list): A list representing the inventory.
    """
    inventory.append(current_room['item'])
    current_room['item'] = None


def handle_command(command: tuple, current_room: dict, inventory: list) -> str:
    """Handles a command.

    Args:
        command (tuple): A tuple containing the command and its arguments.
        current_room (dict): A dictionary representing the current room and its connections.
        inventory (list): A list representing the inventory.

    Returns:
        str: A string containing the new room name.
    """
    new_room_name = current_room['room_name']
    current_command = command[0]
    if current_command == "go":
        new_room_name = handle_direction_command(command, current_room)
    elif current_command == "get":
        handle_item_command(current_room, inventory)
    return new_room_name


def get_win_status(current_room: dict, inventory: list) -> tuple:
    """Figures out the win status.
    
    Args:
        current_room (dict): A dictionary representing the current room and its connections.
        inventory (list): A list representing the inventory.

    Returns:
        tuple: A tuple containing indicators as to whether the player has won or died.
    """
    player_won = player_dead = False
    if current_room['has_robot'] is True:
        player_dead = True
    elif len(inventory) == 6: # player has collected all six items
        player_won = True
    return player_won, player_dead


def display_end_of_game_message(player_won: bool) -> None:
    """Displays a message.
    
    Args:
        player_won (bool): An indicator as to whether the player has won the game.
    """
    if player_won is True:
        print('You have collected all the items! You win!')
    else:
        print('Oh no! The robot!! You died...')


def display_opening_message() -> None:
    """Displays an opening message."""
    opening_message = (
        "-- Disable the Deadly Robot Game --\n"
        "Collect the six items required to build the remote-control which disables the robot to win the game.\n"
        "If you enter the room with the robot you will die. Good luck!\n"
        "----------------- Commands --------------\n"
        "Move commands: go <north|east|south|west>\n"
        "Exit command:  exit\n"
        "-----------------------------------------\n"
    )
    print(opening_message, end="")


def display_status(current_room: dict, inventory: list) -> None:
    """Displays the current status.
    
    Args:
        current_room (dict): A dictionary representing the current room and its connections.
        inventory (list): A list representing the inventory.
    """
    print(f"You are in the {current_room['room_name']}")
    print(f"Inventory: {inventory}")
    if current_room['item'] is not None:
        print(f"You see a {current_room['item']}")


def main() -> None:
    """The main function of the text based game."""
    rooms = {
        "Main Lobby": {
            "room_name": "Main Lobby",
            "north": "Recreation Room",
            "south": "Security Office",
            "east": "Maintenence Room",
            "item": None,
            "has_robot": False,
        },
        "Recreation Room": {
            "room_name": "Recreation Room",
            "south": "Main Lobby",
            "item": "Battery pack",
            "has_robot": False,
        },
        "Security Office": {
            "room_name": "Security Office",
            "north": "Main Lobby",
            "item": "Transmitter",
            "has_robot": False,
        },
        "Maintenence Room": {
            "room_name": "Maintenence Room",
            "west": "Main Lobby",
            "east": "Computer Lab",
            "item": "Electrical tape",
            "has_robot": False,
        },
        "Computer Lab": {
            "room_name": "Computer Lab",
            "north": "3D Printing Lab",
            "east": "Prototype Lab",
            "south": "Parts Supply Room",
            "west": "Maintenence Room",
            "item": "Microchip",
            "has_robot": False,
        },
        "3D Printing Lab": {
            "room_name": "3D Printing Lab",
            "south": "Computer Lab",
            "item": "Remote-control case",
            "has_robot": False,
        },
        "Parts Supply Room": {
            "room_name": "Parts Supply Room",
            "north": "Computer Lab",
            "item": "Wire kit",
            "has_robot": False,
        },
        "Prototype Lab": {
            "room_name": "Prototype Lab",
            "west": "Computer Lab",
            "item": None,
            "has_robot": True,
        },
    }
    inventory = []
    current_room = rooms['Main Lobby']
    command = (None, None)
    player_won = player_dead = False
    display_opening_message()
    while player_won is False and player_dead is False:
        is_valid_command = False
        while is_valid_command is False:
            display_status(current_room, inventory)
            command = get_command()
            is_valid_command = validate_command(command, current_room)
            print("-----------------------------------------")
        new_room_name = handle_command(command, current_room, inventory)
        current_room = rooms[new_room_name]
        player_won, player_dead = get_win_status(current_room, inventory)
    display_end_of_game_message(player_won)


if __name__ == "__main__":
    main()
