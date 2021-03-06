from game.parachute import Parachute
from game.terminal_service import Terminal_Service
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
        self._terminal_service = Terminal_Service()

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
                user_input = self._terminal_service.read_text("Guess a letter [a-z]: ")

                if len(user_input) == 1 and user_input != " ":
                    if user_input.upper() >= "A" and user_input.upper() <= "Z":
                        is_valid = True
                    else:
                        self._terminal_service.write_text_endl("Please, enter a letter from a through z.")
                else:
                    self._terminal_service.write_text_endl("Please, enter a letter from a through z.")

            self._guess = user_input

    def do_updates(self):
        """Updates the status of word, parachute, guesses and game.

        Args:
            self (Director): An instance of Director.
        """

        if self._is_playing:

            is_right_guess = self._word.verify_guess(self._guess)

            if is_right_guess:
                self._word_status = self._word.blank_number
                print(f"Correct Guess!")

                # If the puzzle is solved the game is over.
                if self._word_status == 0:
                    self._is_playing = False
                    print("Congrats you solved the puzzle!")

            else:
                self._parachute.update_parachute()
                self._parachute_status = self._parachute.parachute_status

                if self._parachute_status == 3:
                    print(f"Wrong Guess! \nYou have 3 guesses left")
                elif self._parachute_status == 2:
                    print(f"Wrong Guess! \nYou have 2 guesses left")
                elif self._parachute_status == 1:
                    print(f"Wrong Guess! \nYou have 1 guess left")

                # If the player has no more parachute the game is over.
                elif self._parachute_status == 0:
                    self._is_playing = False
                    print("Game Over!")

    def do_outputs(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        self._word.display_blanks()
        self._parachute.display_parachute()
