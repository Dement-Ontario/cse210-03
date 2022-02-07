from game.terminal_service import Terminal_Service

class Parachute:
    """The parachute to be used in the game.

    The responsibility of a Parachute is to keep track of how many tries 
    the player has left.

    Attributes:
        _parachute (list): list of elements in the parachute.
        parachute_status (int): number of elements in the parachute.
    """

    def __init__(self):
        """Constructs a new Parachute.

        Args:
            self (Parachute): an instance of Parachute.
        """
        self._terminal_service = Terminal_Service()

        self._parachute = []
        self._push("^^^^^^^")
        self._push("")
        self._push("  / \\")
        self._push("  /|\\")
        self._push("   O")
        self._push("  \ /")
        self._push(" \   /")
        self._push(" /___\\")
        self._push("  ___")

        self.parachute_status = 0
        self._update_parachute_status()

    def _push(self, item):
        """Adds an element into the parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """

        self._parachute.append(item)

    def _pop(self):
        """Removes an element from the parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """

        if (self.parachute_status <= 0):
            return False
        return self._parachute.pop()

    def update_parachute(self):
        """Removes an element from the parachute. 
        Updates the status of the parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """

        if self.parachute_status > 1:
            self._pop()
            self._update_parachute_status()
            return True

        elif self.parachute_status == 1:
            self._pop()
            self._pop()
            self._push("   X")
            self._update_parachute_status()
            return True

        else:
            return False

    def _update_parachute_status(self):
        """Update the status of the parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """

        self.parachute_status = len(self._parachute) - 5

    def display_parachute(self):
        """Display parachute in a user friendly format.

        Args:
            self (Parachute): An instance of Parachute.
        """

        self._terminal_service.write_text_endl("")

        for element in range(self.parachute_status + 4, -1, -1):
            self._terminal_service.write_text_endl(self._parachute[element])
