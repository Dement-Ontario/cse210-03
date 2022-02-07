class Terminal_Service:
    """A service that handles terminal operations.

    The responsibility of a TerminalService is to provide input and output operations
    for the terminal.
    """

    def read_text(self, prompt):
        """Directs the user with the given prompt and gets text input from the terminal.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def write_text_endl(self, text):
        """Displays the given text on the terminal. New line is added at the end.

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)

    def write_text(self, text):
        """Displays the given text on the terminal. Space is added at the end.

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text, end=" ")
