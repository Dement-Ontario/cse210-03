import json

FILE_PATH = "../words.json"

class Word:
    """The word to be used in the game.

    The responsibility of a Word is to choose a random word 
    from a list and keep track of correct guesses

    Attributes:
        _chosen_word
        _blanks
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): an instance of Word.
        """
        self._word_list = []
        self._chosen_word = ""
        self.pick_word()

        self._blanks = ""

    def _read_file(self):
        """
        Args:
            self (Board): An instance of Board.
        """

        f = open(FILE_PATH, "r")
        word_dict = json.loads(f.read())
        f.close()

        self._word_list = word_dict["words"]
        

    def pick_word(self):
        """
        Args:
            self (Word): an instance of Word.
        """
        pass
    
    def split_word(self):
        """
        Args:
            self (Word): an instance of Word.
        """
        pass
    
    def create_blanks(self):
        """
        Args:
            self (Word): an instance of Word.
        """
        pass
    
    def verify_guess(self):
        """
        Args:
            self (Word): an instance of Word.
        """
        pass
    
    def update_blanks(self):
        """
        Args:
            self (Word): an instance of Word.
        """
        pass