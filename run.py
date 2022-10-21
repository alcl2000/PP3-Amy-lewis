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
# columns = []
# for ind in range(0, 2):
#    column = OPTIONS.col_values(ind)
#    columns.append(column)
# easy_values = columns[0]
# medium_values = columns[1]
# hard_values = columns[2]


def start_game():
    """
    starts the game by letting the user input a number
    """
    print('1. start game 2. see rules')
    number = input('')
    if number == 1:
        print('starting game...')
    elif number == 2:
        print('displaying rules...')
    else:
        print('please pick a number')

