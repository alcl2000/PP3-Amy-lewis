# Hangman - Testing

## Contents
- [Validator](#Validator)
- [User Stories Testing](#User-Stories-Testing)

---

## Validator
## User Stories Testing

|User Goal | Outcome|
|---|---|
|As a user I want to play a hangman game|The game is easily accessed from the main menu|
|As a user I want to read the rules|The rules page is eaily accessed from the main menu and the rules are set out in an easy to read manner|
|As a user I want to be able to change the difficulty if I find something too hard or easy | From the main menu, when the 'play game' option is selected, users can then pick their chosen difficulty|
|As a user I want the program to respond to my input | The program contains a function that validates input and provides appriopriate responses depending on the data type entered|
|As a user I want accurate and straightforward feedback when I enter input | - When an option is selected from a menu, a short delay is provided to show the user which function is being called - If inappropriate input is entered, functions tell the user how their data should be entered|

## Manual Testing

|Feature| Expected Response | Actual Response| Outcome|
|---|---|---|---|
|Title Page|
|ASCII Art displaying | When the program loads, the ASCII art and 'buttons' load| On start, everything loads correctly | Pass|
|'Run Game' Button | When the number '1' is entered, the game starts | The Game starts when '1' is entered | Pass|
|'Display Rules' Button | When the number '2' is entered, the rules page is displayed | The Rules page is displayed when '2' is entered| Pass|
|'Show Leaderboard' Button|When the number '3' is entered, the rules page is displayed|The Leaderboard is displayed when '3' is entered | Pass|
|'Exit Game' Button| When the number '4' is entered, the program ends| The program ends when '4' is entered| Pass|   
|Input Validation- Data type| When anything other than a number is entered, the program returns an error, and asks for re-entry| When letters or symbols are entered an error is returned, and the function is re-called| Pass|
|Inuput Validation - Value | If a number other than 1-4 is entered, the program returns an error and asks for re-entry| When a number lowerer than 1 or higher than 4 is entered, an error is returned and the function is re-called| Pass|
|Hangman Game Page|
|ASCII Art displaying - Page load| When the Hangman Game starts, the Hangman ASCII art displays with no limbs drawn on, to show the player their progress| On load a blank hangman loads |Pass|
| ASCII Art iteration | When an incorrect answer is entered, the hangman image changes to show how many incorrect guesses have been made| On an incorrect guess, the new hangman becomes standard| Pass|
|Hidden word list| When the game loads, a list of underscores shows to display the word length| On load the correct list displays| Pass|
|Correct letter entry| On a correct letter being entered, the letter replaces its corresponding underscore in the hidden word| When the correct letter is entered, it displays in the word| Pass|
|Correct letter entry - User Validation | When a correct letter is entered, the program prints 'Correct'| On a correct letter entry, the phrase is printed to the terminal | Pass|
|Incorrect letter entry| On an incorrect letter being entered, the program displays the correctly iterated hangman | When an incorrect letter is entered, the hangman changes| Pass|
|Incorrect letter entry - User Validation | When an incorrect letter is entered the phrase incorrect is printed with a display of the remaining incorrect guesses| When the incorrect letter is entered, it displays the message 'incorrect' and the number of remaining guesses| Pass|
|Input validation - Already guessed letters| When a letter is guessed, it is added to an array of already guessed letters, and the user is warned when the letter is guessed again| When a letter is guessed it gets added to the already guessed list and users are warned when they attempt to re-enter it| Pass|
|Input Validation - Numbers/Symbols| When a number or symbol (or any key press that does not contain an English letter) is entered the program should return an error| when anything other than an English letter is entered, the program retuns an error| Pass|
|Game end - Loss| When the user runs out of guesses, the program prints a message and redirects to the scoreboard| The message is printed and the user is redicted correctly|Pass|
|Game end - Win| When all of the correct letters are entered, the message is printed and the user is redirected to the leaderboard page| The message is printed and the user redirected correctly when the list is full of correct letters| Pass|
