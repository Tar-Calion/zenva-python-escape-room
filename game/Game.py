from game.Room1Factory import Room1Factory
from game.Room import Room


class Game:
    def __init__(self):
        self.room = Room1Factory().create_room()

    def check_code(self):
        code = input("Enter the code: ")
        if self.room.check_code(code):
            print("Your code is correct. You have escaped the room. Congratulations!")
            return True
        else:
            print("The code is incorrect.")
            if self.room.get_unsuccessful_tries() >= 3:
                print("You have been locked in the room forever. Game over.")
                # exit the game
                exit()
            print(f"You have {3-self.room.get_unsuccessful_tries()} tries left.")
        return False

    def parse_object_number(self, user_input):
        number = user_input.split(" ")[-1]
        if number.isdigit() and 0 < int(number) <= len(self.room.get_objects()):
            return int(number) - 1
        else:
            return None

    def play(self):
        # print introduction
        print("Welcome to the escape room. You are locked in a room and you need to find the code to escape.")
        print("You can look at, touch and smell objects in the room to find clues.")
        print("You can also check the code to see if you can escape.")

        # main game loop
        while True:
            # print room description
            print("You see the following objects:")
            # print the objects in the room wiht index and names
            for i, obj in enumerate(self.room.get_objects()):
                print(f"{i+1}. {obj.name}")

            # get user input
            user_input = input(
                "What do you want to do? You can 'look', 'touch' or 'smell' an object. For example, you can type 'look at 1'. Type 'exit' to exit the game. Type 'check code' to check the code. ")

            # if user input is "exit", break
            if user_input == "exit":
                print("Goodbye!")
                break

            # if user input is "check code", check the code
            if user_input == "check code":
                success = self.check_code()
                if success:
                    break
                else:
                    continue

            # parse the object number from the user input
            object_index = self.parse_object_number(user_input)
            if object_index is None:
                print(f"Invalid command or object number. Enter a number between 1 and {len(self.room.get_objects())}.")
                continue

            # if user input is "look <object>", call the look method of the object
            if user_input.startswith("look"):
                self.room.get_objects()[object_index].look()
            # if user input is "touch <object>", call the touch method of the object
            elif user_input.startswith("touch"):
                self.room.get_objects()[object_index].touch()
            # if user input is "smell <object>", call the smell method of the object
            elif user_input.startswith("smell"):
                self.room.get_objects()[object_index].smell()
            else:
                # if user input is not recognized, print error message
                print("Invalid interaction. You can 'look', 'touch' or 'smell' an object. For example, you can type 'look at 1'.")
