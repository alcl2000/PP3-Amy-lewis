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


def start_game():
    """
    Checks if the user enters an interger, else raises an error
    If valid number entered, lets user pick game or rules
    """
    print('1. start game 2. see rules')
    while True:
        number = input('')
        try:
            number_int = int(number)
            if number_int == 1:
                print('starting game...')
                choose_difficulty()
                break
            elif number == 2:
                print('displaying rules...')
                break
            else:
                print('Please pick a valid number')
                break
        except ValueError:
            print('Error: Please enter a number')


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
                pick_word(1)
            elif mode == 2:
                print('medium mode selected')
                pick_word(2)
            elif mode == 3:
                print('hard mode selected')
                pick_word(3)
            else:
                print('Please select a difficulty ')
        except ValueError:
            print('Please enter a valid number')


def pick_word(difficulty):
    """
    takes the value of choose_difficulty to select the word for hangman
    """
    choice = random.randrange(13)
    if difficulty == 1:
        print(easy_values(choice))
    elif difficulty == 2:
        print(medium_values(choice))
    elif difficulty == 3:
        print(hard_values(choice))


start_game()