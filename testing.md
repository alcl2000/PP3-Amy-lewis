# Hangman - Testing

## Contents
- [Validator](#Validator)
- [User Stories Testing](#User-Stories-Testing)

---

## Validator

The program produces no errors with the CI PEP8 validator 

The program also produces no errors with the Pycodestyle linter installed

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
|Rules Page|
|Page display and load | When the page loads the rules automatically display with the buttons below| When the rules option is selected the rules and buttons load correctly | Pass|
|'Return Home' button | When '1' is entered the user is taken back to the home page| When the number one is entered the user is redirected home correctly| Pass|
|Exit Game button| When '2' is entered the program exits| The program exits without issue when '2' is entered| Pass|
|Input validation - Type| When the user doesn't enter a number, the program displays an error and then re-calls itself | When a letter or symbol is entered, an error is displayed and the function is re-called|Pass|
| Input Validation - Value | When the user enters a number other than 1 or 2 an error is displayed and the function re-called | When an incorrect letter is entered, the program displays an error and re-calls itself|
|Leader Board|
|Function call- from home| When the '3' button is pressed on the home page the top three scores should be called with the names of the users |When the function is called from the home page the top three are printed correctly |Pass|
|Function call - Game Win| When a user wins the game, their score is displayed and they are asked if they would like to add it to the board | The function is called correctly when the user wins the game |Pass|
|Function call - Game Loss | If the user loses their game, a message is printed before showing the top three scores| The message and scoreboard are both printed correctly when the user loses a game| Pass|
|Add score to leaderboard | On a game win, the program prints a message and gives the option to add to leaderboard with a name | When the user wins, they are able to enter their score, the leaderboard updates correctly and displays the new scores| Pass|
| Return Home button| If '1' is entered the user is returned home | If '1' is entered the main menu is returned to correctly| Pass|
|End Game button| If '2' is entered the program should end|If '2' is entered the program is exited | Pass|
|Name Input Validation | If the string is longer than 3 an error should be returned and the function recalled | If the string is too long, the function returns an error and re-calls itself |Pass|
|Input Validation - Data type| When the user enters a number on the screen, it check the data type and only allows the program to continue with a correct data type | The data is validated correctly and if a string is entered the program returns an error and re-calls |Pass|
|Input Validation - Data Value | When the user enters a number other than 1 or 2 it returns an input error and re-calls itself | When an incorrect number is enters, the program returns an error and re-prints the leaderboard| Pass|

