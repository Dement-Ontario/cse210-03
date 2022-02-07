from game.parachute import Parachute
# from game.terminal import Terminal
from game.word import Word


class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """

        self._is_playing = True

        self._word = Word()
        self._word_status = self._word.blank_number

        self._parachute = Parachute()
        self._parachute_status = self._parachute.parachute_status

        self._guess = ""

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        self._word.display_blanks()
        self._parachute.display_parachute()

        while self._is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user for guess.

        Args:
            self (Director): An instance of Director.
        """

        if self._is_playing:

            is_valid = False

            while not is_valid:
                user_input = input("Guess a letter [a-z]: ")

                if len(user_input) == 1 and user_input != " ":
                    is_valid = True
                else:
                    print("Please, enter a letter from a through z.")

            self._guess = user_input

    def do_updates(self):
        """Updates the status of word, parachute and game.

        Args:
            self (Director): An instance of Director.
        """

        if self._is_playing:

            is_right_guess = self._word.verify_guess(self._guess)

            if is_right_guess:
                self._word_status = self._word.blank_number

                # If the puzzle is solved the game is over.
                if self._word_status == 0:
                    self._is_playing = False

            else:
                self._parachute.update_parachute()
                self._parachute_status = self._parachute.parachute_status

                # If the player has no more parachute the game is over.
                if self._parachute_status == 0:
                    self._is_playing = False

    def do_outputs(self):
        """
        Args:
            self (Director): An instance of Director.
        """

        if self._is_playing:

            self._word.display_blanks()
            self._parachute.display_parachute()
        
        else:
            self._parachute.display_parachute()
