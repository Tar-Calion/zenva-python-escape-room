from game.RoomObject import RoomObject


class Room:
    def __init__(self, exit_code, objects: list[RoomObject]):
        self.exit_code = exit_code
        self.objects = objects
        self.tries = 0

    def check_code(self, code):
        if code == self.exit_code:
            return True
        else:
            self.tries += 1
            return False

    def get_unsuccessful_tries(self):
        return self.tries

    def get_objects(self):
        return self.objects
