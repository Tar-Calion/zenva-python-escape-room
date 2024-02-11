# zenva-python-escape-room
Escape room game

## Project definition
This project is a simple text-based escape room game. The player is locked in a room and must open the door to escape. The room contains a number of objects that the player can interact with. The final goal is to find the three-digit code that unlocks the door. The player can interact with the objects in the room to find the clues about the code.

There are five objects in the room. The objects can be interacted with in three ways: looking, touching and smelling. Each interaction can be meaningless or provide a clue about a digit of the code or the position of the digit in the code.

The game will print the description of the room and the objects. The player can then choose to interact with an object. The game will then print the result of the interaction. The player can then choose to interact with another object or to try to unlock the door. There is also an option to quit the game.

The game will end when the player wins or loses. The player wins if the code is correct. The player loses if the code is guessed incorrectly three times or if the player decides to quit.

## Project design

Main objects:
- Game: the main class that controls the game
- Room: the class that represents the room
    - RoomObjects
    - Exit code
    - tracks the number of attempts to unlock the door
- RoomObject: the class that represents the objects in the room
    - Description
    - Interactions
  

## Clues

The code is 379.
The objects are: a painting, a statue of an angel, a fireplace, a comfy chair and a plant.

There are six clues, one for each digit of the code and one for the position of the digit in the code.
1. Touching the comfy chair reveals a peculiar coin with value of 3 pesos.
2. Looking at the painting reveals a small plaque with the inscription "The three primal gods" (hints at "3" being the first digit).
3. Touching the angel statue reveals a roman numeral "VII" at its back.
4. Looking at the fireplace reveals a book with the title "After the gods came the angels" (hints at "7" being the second digit).
5. Smelling the plant makes the player sneeze and a small piece of paper falls from the pot. The paper has the number "9" written on it.
6. Looking at the chair reveals a prominent plague with the inscription "Use to wind down after 9 p.m. before going to bed" (hints at "9" being the last digit).

## Running the game
run the game by running the main.py file
```python
python main.py
```
