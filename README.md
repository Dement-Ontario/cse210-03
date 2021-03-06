# Jumper
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

## Getting Started
---
Make sure you have Python 3.9.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 jumper 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- jumper              (source code for game)
  +-- game              (specific classes)
    +-- director.py     (Director class)
    +-- parachute.py    (Parachute class)
    +-- terminal.py     (Terminal class)
    +-- word.py         (Word class)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.9.0

## Authors
---
* Joseph Toronto (tor21019@byui.edu)
  * Coded Terminal Service class, modified Director class to put
Terminal Service to use, made blank letters display
regardless of the game's status

* Eddy Sosa Lora (eddysosa@byui.edu)
  * Coded Director, Parachute and Word classes based on the design done by Joseph and Stephen. Fixed bug with uppercase and lowercase letters.

* Stephen Port (por21022@byui.edu)
  * Added code to tell the user exactly many guesses they have in the terminal output, along with game is over or puzzle is solved.
* Atubo Gift Atubo (atu21001@byui.edu)
* Mark Jovit R. Colonia (markcolonia12@gmail.com)