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

