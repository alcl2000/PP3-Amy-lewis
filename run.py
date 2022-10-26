import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hang-man-choices')
OPTIONS = SHEET.worksheet('options')

# Columns/Word selection
easy_values = OPTIONS.col_values(1)
medium_values = OPTIONS.col_values(2)
hard_values = OPTIONS.col_values(3)


def check_interger(x):
    """
    checks if the user input is or isn't an interger and returns t/f values 
    dependant on that 
    """
    try:
        int(x)
        return True
    except ValueError:
        return False


def start_game():
    """
    Checks if the user enters an interger, else raises an error
    If valid number entered, lets user pick game or rules
    """
    print('1. start game 2. see rules')
    number = input('')
    interger = check_interger(number)
    if interger is True:
        if interger == 1:
            print('starting game...')
            return True
        elif number == 2:
            print('displaying rules...')
            return False
        else:
            print('Please pick a valid number')
    else:
        print('Please enter a number')


def display_rules():
    """
    will display the rules for the player when this option is selected
    """
    pass


def choose_difficulty():
    """
    picks the difficulty from one to three, and picks a word from the column
    """
    print('Select your difficulty\n 1. Easy 2. Medium 3. Hard')
    while True:
        mode = input('')
        mode = int(mode)
        try:
            if mode == 1:
                print('easy mode selected')
                return 1
            elif mode == 2:
                print('medium mode selected')
                return 2
            elif mode == 3:
                print('hard mode selected')
                return 3
            else:
                print('Please select a difficulty ')
        except ValueError:
            print('Please enter a valid number')
        break


def pick_word(difficulty):
    """
    takes the value of choose_difficulty to select the word for hangman
    """
    choice = random.randrange(12)
    if difficulty == 1:
        secret_word = easy_values[choice]
    elif difficulty == 2:
        secret_word = medium_values[choice]
    elif difficulty == 3:
        secret_word = hard_values[choice]
    return secret_word


def display_word(secret_word):
    """
    breaks the selected word down into a list to then be used in hangman
    """
    letters = []
    to_test = []
    for letter in range(len(secret_word)):
        letters.append(secret_word[letter])
    for letter in letters:
        to_test.append('_')
    print(to_test)
    hangman(letters, to_test)


def hangman(letters, to_test):
    incorrect_guesses = 10
    # y = letters.len() 
    while incorrect_guesses > 0:
        guess = input('Choose a letter:')
        is_letter = check_interger(guess)
        if is_letter is False:
            for letter in letters:
                if guess == letter:
                    print('Correct letter!')
                    break
                else:
                    print('Incorrect Guess')
        else:
            print('Please enter a Valid letter')
            incorrect_guesses -= 1
    end_game()
                

def end_game():
    pass


def main():
    """
    main function calls
    """
    run_game = start_game()
    if run_game is True:
        difficulty = choose_difficulty()
        secret_word = pick_word(difficulty)
        display_word(secret_word)
    else:
        display_rules()


main()
