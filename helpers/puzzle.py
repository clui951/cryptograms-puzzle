import re

class Puzzle:
    def __init__(self, input_string):
        self.input_string = input_string.upper()
        self.input_list = list(input_string)

        self.input_char_to_output_char = None
        self.input_char_to_pos_list = None
        self.reset_output_list()


    def reset_output_list(self):
        """
        Resets char mapping and output
        :return: None
        """
        self.input_char_to_output_char = {}

        self.input_char_to_pos_list = {}
        self.output_list = self.input_list.copy()

        for i in range(len(self.output_list)):
            c = self.output_list[i]
            if not c.isalpha():
                continue

            # build input_char to ... mappings
            if c not in self.input_char_to_output_char:
                self.input_char_to_output_char[c] = None
                self.input_char_to_pos_list[c] = [i]
            else:
                self.input_char_to_pos_list[c].append(i)

            # build output_list
            self.output_list[i] = "_"


    def map_char(self, input_char, output_char):
        """
        :param input_char: letter to map from
        :param output_char: letter to map to
        :return: True/False if successfully mapped
        """
        input_char = input_char.upper()
        output_char = output_char.upper()

        if input_char not in self.input_char_to_output_char.keys():
            return False

        self.input_char_to_output_char[input_char] = output_char
        for i in self.input_char_to_pos_list[input_char]:
            self.output_list[i] = output_char
        return True


    def all_letters_mapped(self):
        """
        :return: True if all input chars mapped to a output char; else False
        """
        return None not in self.input_char_to_output_char.values()


    def generate_output_string(self):
        """
        :return: string representing output given current char mapping
        """
        return "".join(self.output_list)


    def print_state(self):
        """
        prints input string and output string
        :return: None
        """
        print(self.input_string)
        print(self.generate_output_string())