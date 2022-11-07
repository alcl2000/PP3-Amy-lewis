# Hangman Python Game

This project is a simple hangman game created in python

[Live Link]()

## Contents

- [Flowcharts](#Flowcharts)
- [User Experience](#User-Experience)
    -[User Interface](#user-interface)
- [Project Goals](#project-goals)

## FlowCharts
![The top half of a flowchart showing the beginning actions of starting the hangman game](assets/readme/flowchart-1.jpg)<br>
![The bottom half of a flowcchart showing the ending actions of the hangman game](assets/readme/flowchart-2.jpg)


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

## Features

### ASCII art 

- The game feautures various peices of ASCII art throughout

- The opening page has A picture of Alcatraz prison which sets the users up for the game they're going to play 

- The hangman art iterates on an incorrect answer, providing clear feedback to users on how their guesses are being scored

### Entry Page

- The entry page 

## Bug Fixes

### Secret word not matching the user input

The secret word is being split into a list, however the input is not being matched up to the correspinding letter in the list.

### No way to handle duplicate letters in words

### Game not automatically ending on a correct answer

- handled by iterating through to_test, and testing if _ remained