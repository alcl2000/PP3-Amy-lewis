import gspread
from google.oauth2.service_account import Credentials

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
    starts the game by letting the user input a number
    """
    print('1. start game 2. see rules')
    number = input('')
    if number == '1':
        print('starting game...')
        choose_difficulty()
    elif number == '2':
        print('displaying rules...')
    else:
        print('please pick a number')


def choose_difficulty():
    """
    picks the difficulty from one to three, and picks a word from the column
    """
    print('Select your difficulty\n 1. Easy 2. Medium 3. Hard')
    mode = input('')
    if mode == '1':
        print('easy mode selected')
    elif mode == '2':
        print('medium mode selected')
    elif mode == '3':
        print('hard mode selected')
    else:
        print('please select a number')


start_game()