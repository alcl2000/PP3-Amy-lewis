import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Spreadsheets values
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hang-man-choices')
OPTIONS = SHEET.worksheet('options')

HANGMAN_PICS = ['''
     +---+
     o   |
    /|\  |
    / \  |
     =====''', '''
     +---+
     o   |
    /|\  |
    /    |
     =====''', '''
    +---+
    o   |
   /|\  |
        |
    =====''', '''
    +---+
    o   |
   /|   |
        |
    =====''', '''
   +---+
   o   |
   |   |
       |
    ====''', '''
   +---+
   o   |
       |
       |
    ====''', '''
   +---+
       |
       |
       |
    ====
''']

# Columns/Word selection
easy_values = OPTIONS.col_values(1)
medium_values = OPTIONS.col_values(2)
hard_values = OPTIONS.col_values(3)

# Universal for gameplay
letters = []
to_test = []
already_guessed = []


def check_interger(x):
    """
    checks if the user input is or isn't an interger and returns t/f values 
    dependant on that 
    """
    if len(x) == 1:
        try:
            int(x)
            return True
        except ValueError:
            return False
    else:
        return None


def start_game():
    """
    Checks if the user enters an interger, else raises an error
    If valid number entered, lets user pick game or rules
    """
    print(''' 
    /_ /  /\   /\  / /```     /\ /\   /\   /\  / 
   /  /  /--\ /  \/ /__``/   /  |  \ /--\ /  \/
    ''')
    print('''
                   ALCATRAZ  __
                    PRISON  /__\             
                ____________|##|             
                |_|_|_|_|_|_|  |             
                |_|_|_|_|_|_|__|            
                A@\|_|_|_|_|_|/@@Aa          
            aaA@@@@@@@@@@@@@@@@@@@aaaA     
            A@@@@@@@@@@@DWB@@@@@@@@@@@@A    
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ''')
    print('1. start game 2. see rules')
    number = input('')
    interger = check_interger(number)
    if interger is True:
        number = int(number)
        if number == 1:
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
    print(''' 
    /_ /  /\   /\  / /```     /\ /\   /\   /\  / 
   /  /  /--\ /  \/ /__``/   /  |  \ /--\ /  \/
    ''')
    print('''
    This a game of hangman
    1. From the main menu select "Play Game" by pressing 1
    2. Select your game mode
    - Either easy, medium or hard by pressing 1, 2, or 3
    - Easy mode has the shortest words, medium slightly longer etc
    3. When prompted please enter a letter into the terminal
    4. The program will then test your answer against the scecret word
    5. If your answer is correct, it will be displayed in the secret word
    6. If your answer is incorrect, a line will be added to the hangman
    7. You only get 6 incorrect guesses - so be careful!''')
    print('''
    If you win, you can add your score to the leader board!
    ''')
    print('''
    1. Return home''')
    x = input('')
    if check_interger(x) is True:
        start_game()
    else:
        start_game()


def choose_difficulty():
    """
    picks the difficulty from one to three, and picks a word from the column
    """
    print('''
            /`````````````\`
            | H E L P  M E |
            `\............./
                 |
    ================================
    ||     ||     ||     ||     ||
    ||    _||     ||     ||_    ||
    ||   (__D     ||     C__)   ||
    ||   (__D     ||     C__)   ||
    ||   (__D     ||     C__)   ||
    ||   (__D     ||     C__)   ||
    ||     ||     ||     ||     ||
    ================================
    ''')
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
    for letter in range(len(secret_word)):
        letters.append(secret_word[letter])
    for letter in letters:
        to_test.append('_')
    print(HANGMAN_PICS[6])
    print(to_test)
    hangman(letters, to_test)


def hangman(letters, to_test):
    incorrect_guesses = 6
    while incorrect_guesses >= 0:
        guess = input('Choose a letter:')
        is_letter = check_interger(guess)
        print(letters)
        print(HANGMAN_PICS[incorrect_guesses])
        print(to_test)
        if is_letter is False:
            check_letters = check_letter(guess, letters)
            if check_letters is True:
                pass
            else:
                incorrect_guesses -= 1
        else:
            print('Please enter a Valid letter')
    end_game()


def check_letter(x, letters):
    """
    Function to check all of the letters in the word array
    before printing or returning the result to the user
    """
    for ind in letters:
        if x == already_guessed[ind]:
            print('Letter already guessed! Please enter a different one')
        else:
            already_guessed.append(x)
            print(already_guessed)
            for letter in letters:
                if x == letter:
                    print('Correct letter!')
                    return True
                else:
                    print('Incorrect Guess')
                    return False
        

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
