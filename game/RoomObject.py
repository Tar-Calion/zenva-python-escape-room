class RoomObject:
    def __init__(self, name, look_text, feel_text, smell_text):
        self.name = name
        self.look_text = look_text
        self.feel_text = feel_text
        self.smell_text = smell_text

    def look(self):
        print(f"\n  >>> You look at the {self.name}. {self.look_text}. <<<\n")

    def touch(self):
        print(f"\n  >>> You touch the {self.name}. {self.feel_text}. <<<\n")

    def smell(self):
        print(f"\n  >>> You smell the {self.name}. {self.smell_text}. <<<\n")
