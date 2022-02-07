import json
import random

FILE_PATH = "cse210-03/words.json"


class Word:
    """The word to be used in the game.

    The responsibility of a Word is to choose a random word 
    from a list and keep track of correct guesses.

    Attributes:
        _word_list (list): list of words.
        chosen_word (string): chosen word from the list of words.
        _letters (list): list of letters in the chosen word.
        _blanks (list): list of blanks for each letter in the chosen word.
        blank_number (int): number of blanks in the chosen word.
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): an instance of Word.
        """
        self._word_list = []
        self._get_word_list()

        self.chosen_word = ""
        self._pick_word()

        self._letters = []
        self._split_word()

        self._blanks = []
        self.blank_number = 0
        self._create_blanks()

    def _get_word_list(self):
        """ Get list of words from FILE_PATH.

        Args:
            self (Board): An instance of Board.
        """

        f = open(FILE_PATH, "r")
        word_dict = json.loads(f.read())
        f.close()

        self._word_list = word_dict["words"]

    def _pick_word(self):
        """Pick random word from the list of words.

        Args:
            self (Word): an instance of Word.
        """
        assert len(self._word_list) > 0

        random_index = random.randint(0, len(self._word_list) - 1)
        self.chosen_word = self._word_list[random_index]

    def _split_word(self):
        """Split chosen word into list of letters.

        Args:
            self (Word): an instance of Word.
        """
        assert self.chosen_word != ""

        self._letters = []
        for letter in self.chosen_word:
            self._letters.append(letter)

    def _create_blanks(self):
        """Assign a black space for each letter in the chosen word.
        Update the number of blanks.

        Args:
            self (Word): an instance of Word.
        """
        assert self.chosen_word != ""

        self._blanks = []
        for letter in self.chosen_word:
            self._blanks.append("_")
            self.blank_number += 1

    def verify_guess(self, guess):
        """Verify guess against chosen word. Assign guess if right. 
        Update number of blanks.

        Args:
            self (Word): an instance of Word.
        """

        assert type(guess) is str
        assert len(guess) == 1

        is_repeat = False
        for letter in self._blanks:
            if letter == guess:
                is_repeat = True
                break

        starting_number = self.blank_number

        if not is_repeat:
            for index in range(len(self._letters)):
                if self._letters[index].upper() == guess.upper():
                    self._blanks[index] = self._letters[index]
                    self.blank_number -= 1

        if starting_number != self.blank_number:
            return True
        return False

    def display_blanks(self):
        """Display blanks in a user friendly format.
        
        Args:
            self (Word): an instance of Word.
        """

        for index in range(len(self._blanks)):
            print(self._blanks[index], end=" ")

        print()