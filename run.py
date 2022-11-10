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
LEADERBOARD = SHEET.worksheet('leaderboard')

# ACSII ART
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

TITLE = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
    """


# Columns/Word selection
easy_values = OPTIONS.col_values(1)
medium_values = OPTIONS.col_values(2)
hard_values = OPTIONS.col_values(3)

# Universal for gameplay
position_of_letter = []


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
    print(TITLE)
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
    print('''
           1. Start game 2. See rules
         3. See leaderboard 4.Exit Game
        ''')
    number = input('')
    interger = check_interger(number)
    if interger is True:
        number = int(number)
        if number == 1:
            print('Starting game...')
            return True
        elif number == 2:
            print('Displaying rules...')
            return False
        elif number == 3:
            print('Displaying leaderboard...')
            show_leaderboard(0)
        elif number == 4:
            print('Exiting Game...')
            exit()
        else:
            print('Please pick a valid number')
    else:
        print('Please enter a number')


def display_rules():
    """
    will display the rules for the player when this option is selected
    """
    print(TITLE)
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
        main()
    else:
        main()


def choose_difficulty():
    """
    picks the difficulty from one to three, and picks a word from the column
    """
    print('''
            /``````````````\`
            | H E L P  M E |
            \............./
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
    choice = random.randrange(25)
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
    # Clears all lists when user plays again
    letters = []
    to_test = [] 
    
    for letter in range(len(secret_word)):
        letters.append(secret_word[letter])
    for letter in letters:
        to_test.append('_')
    print(HANGMAN_PICS[6])
    print(to_test)
    hangman(letters, to_test)


def hangman(letters, to_test):
    """
    Main game loop
    Takes the secret word and covered up word list
    Tests user responses against the secret word
    Reveals the secret word when guessed
    """ 
    incorrect_guesses = 7
    already_guessed = []

    while '_' in to_test and incorrect_guesses > 0:
        user_guess = input('Choose a letter: ')   
        is_letter = check_interger(user_guess)
        print(letters)
        print(HANGMAN_PICS[(incorrect_guesses - 1)])
        correct_guess = 0
        if is_letter is False:
            user_guess = user_guess.lower()
            if user_guess not in already_guessed:
                x = 0
                print(already_guessed)
                already_guessed.append(user_guess)
                for letter in letters:
                    if user_guess == letter:
                        to_test[x] = user_guess
                        correct_guess += 1
                    x += 1 
                print(to_test)
                if correct_guess > 0:
                    print('Correct answer!')
                else:
                    incorrect_guesses -= 1
                    print('Incorrect answer, please try again')
                    print(f'You have: {(incorrect_guesses)} guesses remaining')
            else:
                print('Letter already guessed\n Please try again!')
        else:
            print('Please enter a valid letter')
    end_game(incorrect_guesses, letters)


def end_game(incorrect_guesses, letters):
    """
    ends the game and displays the user's score
    """
    score = incorrect_guesses * len(letters)
    print(TITLE)
    print('Game Over!!')
    if score > 0:
        print(f'Congratulations!\nYour score is: {score}')
        print('Going to leaderboard...')
        show_leaderboard(score)
    else:
        print("Sorry! You weren't able to save the man")
    print('Play again? \n Y. Play again N. End Game')
    play_again = input('')
    play_again = play_again.lower()
    # Input validation 
    is_valid = check_interger(play_again)
    if is_valid is False:
        if play_again == 'y':
            main()
        elif play_again == 'n':
            pass
        else:
            print('Please enter either Y or N')
    else:
        print('Please only enter Y or N')


def show_leaderboard(score):
    """
    Shows the top three scores
    Allows user to add their name to the leaderboard if they scored high enough
    """
        # Leaderboard values
    first_place = LEADERBOARD.acell('B1').value
    second_place = LEADERBOARD.acell('B2').value
    third_place = LEADERBOARD.acell('B3').value
    first_score = LEADERBOARD.acell('A1').value
    second_score = LEADERBOARD.acell('A2').value
    third_score = LEADERBOARD.acell('A3').value

    LEADERBOARD_GRAPHIC = f'''
                    Leaderboard:
                    1. {first_place} . {first_score}
                    2. {second_place} . {second_score}
                    3. {third_place} . {third_score}
        '''

    print(TITLE)
    print(LEADERBOARD_GRAPHIC)
    if score > int(third_score): 
        print(f'Your score is: {score}') 
        print('Would you like to add your score to the leaderboard?')
        y_n = input('Y. Yes N. No\n')
        if y_n == 'y':
            add_to_leaderboard(score, first_score, second_score, third_score)
        else:
            main()
    main_menu = input('Return home?\n Y. yes N. no\n')
    if main_menu == 'y':
        main()
    else:
        print(LEADERBOARD_GRAPHIC)


def add_to_leaderboard(score, first_score, second_score, third_score):
    """
    Checks which specific score the user has beaten 
    and allows them to add their name to the sheets
    """
    name = input('What is your name?:')
    name = name.upper()
    if len(name) == 3:
        if score >= int(first_score):
            LEADERBOARD.insert_row([score, name], index = 1)
        elif score >= int(second_score):
            LEADERBOARD.insert_row([score, name], index = 2)
        elif score >= int(third_score):
            LEADERBOARD.insert_row([score, name], index = 3)
        else:
            print('Sorry your score is not high enough to go on the leader board')
    else:
        print('Name must be 3 chars long')
    show_leaderboard(0)


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


# main()
show_leaderboard(28)