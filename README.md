
# Disable the Deadly Robot Game

This is a text-based game where the player's objective is to collect six items required to build a remote-control that disables a deadly robot. The player must avoid entering the room with the robot, as it will result in death. Good luck!

## Commands

- Move command: `go <north|east|south|west>`
- Get item command:  `get <item name>`

## Instructions

1. Run `python3 TextBasedGame.py` to start the game.
2. Enter commands to navigate through rooms, collect items, and complete the game objectives.
3. The game will display the current room, inventory, and available actions.
4. Follow the prompts and continue entering commands until the game ends.
5. The game ends when the player either collects all the required items and wins or encounters the deadly robot and dies.
6. Upon game completion, the game will display an end-of-game message.

## Game Logic Overview

The code uses a dictionary named `rooms` to represent the rooms in the game. Each room has a name, connections to other rooms, an item (if any), and a flag indicating the presence of the deadly robot.

The main logic of the game is implemented in the `main()` function. The player's progress, current room, inventory, and game status are tracked using variables.

The game prompts the player for commands and validates them based on the current room's state. Valid commands include movement commands (`go <direction>`) and item-related commands (`get <item>`).

The game continues until the player either wins by collecting all six items or dies by encountering the deadly robot. The final status of the game is displayed, indicating whether the player won or lost.

Have fun playing the Disable the Deadly Robot Game!
