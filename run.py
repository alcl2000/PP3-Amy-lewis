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
        except ValueError:
            print('Error: Please enter a number')


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