# Aidan Farhi - 2023-06-13

def get_command() -> tuple:
    """Prompts the user to enter a command and returns it as a tuple.

    Returns:
        tuple: A tuple containing the command and its arguments.
    """
    command = input("Enter Command > ")
    command = tuple(command.split())
    return command


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
    if len(command) > 2:
        print("Invalid input!")
        valiation_result = False
    elif command[0] not in ("exit", "go"):
        print("Invalid input!")
        valiation_result = False
    elif command[0] == "go":
        valiation_result = validate_move_command(command, current_room)
    return valiation_result


def handle_direction_command(command: tuple, current_room: dict) -> str:
    """Handles a direction command.

    Args:
        command (tuple): A tuple containing the command and its arguments.
        current_room (dict): A dictionary representing the current room and its connections.

    Returns:
        dict: The new room after moving in the specified direction.
    """
    direction = command[1]
    new_room = current_room[direction]
    return new_room


def handle_command(command: tuple, current_room: dict) -> tuple:
    """Handles a command.

    Args:
        command (tuple): A tuple containing the command and its arguments.
        current_room (dict): A dictionary representing the current room and its connections.

    Returns:
        tuple: A tuple containing the new room and an indicator for program exit.
    """
    new_room = current_room
    exit_program = False
    current_command = command[0]
    if current_command == "go":
        new_room = handle_direction_command(command, current_room)
    else:
        exit_program = True
    return new_room, exit_program


def main() -> None:
    """The main function of the text based game."""
    rooms = {
        "Main Lobby": {
            "north": "Recreation Room", 
            "south": "Security Office",
            "east": "Maintenence Room",
            "item": None,
            "has_robot": False
        },
        "Recreation Room": {
            "south": "Main Lobby", 
            "item": "Battery pack",
            "has_robot": False
        },
        "Security Office": {
            "north": "Main Lobby",
            "item": "Transmitter",
            "has_robot": False
        },
        "Maintenence Room": {
            "west": "Main Lobby",
            "east": "Computer Lab",
            "item": "Elecrical tape",
            "has_robot": False
        },
        "Computer Lab": {
            "north": "3D Printing Lab",
            "east": "Prototype Lab",
            "south": "Parts Supply Room",
            "west": "Maintenence Room",
            "item": "Microchip",
            "has_robot": False
        },
        "3D Printing Lab": {
            "south": "Computer Lab",
            "item": "Remote-control case",
            "has_robot": False
        },
        "Parts Supply Room": {
            "north": "Computer Lab",
            "item": "Wire kit",
            "has_robot": False
        },
        "Prototype Lab": {
            "west": "Computer Lab",
            "item": None,
            "has_robot": True
        }
    }
    inventory = []
    current_room = "Main Lobby"
    opening_message = (
        "-- Disable the Deadly Robot Game --\n"
        "Collect the six items required to build the remote-control which disables the robot to win the game.\n"
        "If you enter the room with the robot you will die.\n"
        "----------------- Commands --------------\n"
        "Move commands: go <north|east|south|west>\n"
        "Exit command:  exit\n"
        "-----------------------------------------\n"
    )
    print(opening_message, end="")
    command = (None, None)
    exit_program = False
    while exit_program is False:
        is_valid_command = False
        while is_valid_command is False:
            print(f"You are in the {current_room}")
            command = get_command()
            is_valid_command = validate_command(command, rooms[current_room])
            print("-----------------------------------------")
        current_room, exit_program = handle_command(command, rooms[current_room])
    print("Thanks for playing!")


if __name__ == "__main__":
    main()