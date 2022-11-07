# Hangman Python Game

This project is a simple hangman game created in python

[Live Link]()

## Contents

- [Wireframes](#Wireframes)
- [User Experience](#User-Experience)
    -[User Interface](#user-interface)
- [Project Goals](#project-goals)

## Wireframes
    <details open>
    <summary>Flowcharts</summary>
    ![The top half of a flowchart showing the beginning actions of starting the hangman game](assets/readme/flowchart-1)<br>
    ![The bottom half of a flowcchart showing the ending actions of the hangman game](assets/readme/flowchart-2.jpg)
    </details>

## User Experience

### User Stories

- As a user I want to play a hangman game
- As a user I want to read the rules and be able to understand the game 
- As a user I want to be able to change the difficulty if I find something too hard or easy
- As a user I want the program to respond to my input
- As a user I want accurate and straightforward feedback when I enter input

## Project Goals

- As the site owner I want the user to have a fun experience.
- As the site owner I want the game to be functional with no bugs or errors.

## Bug Fixes

### Secret word not matching the user input

The secret word is being split into a list, however the input is not being matched up to the correspinding letter in the list.

### No way to handle duplicate letters in words

### Game not automatically ending on a correct answer

- handled by iterating through to_test, and testing if _ remained