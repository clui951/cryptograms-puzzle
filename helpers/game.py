import enum
import string
import sys

from helpers.puzzle import Puzzle


class Actions(enum.Enum):
    MAP = "map"
    UNMAP = "unmap"
    RESET = "reset"
    QUIT = "quit"

    @classmethod
    def get_actions_string(cls):
        return ", ".join([a.value for a in list(Actions)])

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

class Game:
    def __init__(self):
        self.puzzle = None
        self.quit = False


    def create_game(self):
        input_string = input("Enter cryptogram here:\n")
        self.puzzle = Puzzle(input_string)


    def run(self):
        while not self.quit and not self.puzzle.output_matches_solution():
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            self.puzzle.print_state()

            action_string = input("Choose action ({}): ".format(Actions.get_actions_string()))
            if not Actions.has_value(action_string):
                print("Invalid action!")
                continue

            action = Actions(action_string)
            self.action_fanout(action)


    def action_fanout(self, action):
        if action == Actions.MAP:
            self.do_map_action()
        elif action == Actions.RESET:
            self.do_reset_action()
        elif action == Actions.QUIT:
            self.do_quit_action()
        else:
            print("WARNING: ACTION NOT YET IMPLEMENTED")


    def do_map_action(self):
        # Prompt for input char
        input_char = input("Enter letter to map: ").upper()
        if len(input_char) != 1 and input_char.upper() not in string.ascii_letters:
            print("Letter must be a single alphabetical character.")
            return

        # Prompt for output char
        output_char = input("Enter letter to map {0} to: ".format(input_char)).upper()
        if len(output_char) != 1 and output_char.upper() not in string.ascii_letters:
            print("Letter must be a single alphabetical character.")
            return

        # Perform map
        if not self.puzzle.map_char(input_char, output_char):
            print("Mapping {0} to {1} {2}".format(input_char, output_char, "failed."))
            return
        print("Mapping {0} to {1} {2}".format(input_char, output_char, "succeeded."))


    def do_reset_action(self):
        self.puzzle.reset()


    def do_quit_action(self):
        self.quit = True