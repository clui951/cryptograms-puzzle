import string

from helpers.puzzle import Puzzle

class Game:
    def __init__(self):
        self.puzzle = None


    def create_game(self):
        input_string = input("Enter cryptogram here:\n")
        self.puzzle = Puzzle(input_string)


    def run(self):
        while not self.puzzle.all_letters_mapped():
            input_char, output_char = self.prompt_char_map()

            if not self.puzzle.map_char(input_char, output_char):
                print("Mapping {0} to {1} {2}".format(input_char, output_char, "failed."))
                continue
            print("Mapping {0} to {1} {2}".format(input_char, output_char, "succeeded."))

            self.puzzle.print_state()


    def prompt_char_map(self):
        print()
        input_char = None
        while input_char == None:
            input_char = input("Enter letter to map: ").upper()
            if len(input_char) == 1 and input_char.upper() in string.ascii_letters:
                break
            print("Letter must be a single alphabetical character.")

        output_char = None
        while output_char == None:
            output_char = input("Enter letter to map {0} to: ".format(input_char)).upper()
            if len(output_char) == 1 and output_char.upper() in string.ascii_letters:
                break
            print("Letter must be a single alphabetical character.")

        return input_char.upper(), output_char.upper()