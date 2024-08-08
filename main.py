from game_art import welcome_art, user_wins, computer_wins, bye_art, draw_art
from game_data import game_board, game_board_position, winning_combination
import random
import time
# Remembering user's and computer's paces in the game. 
user_paces = []
computer_paces = []
# Print the welcome message.
print(welcome_art)
# Print the game notice.
print(r"""
Please note the position numbering for the game
----------------------
    1   |   2   |   3   
----------------------
    4   |   5   |   6
----------------------
    7   |   8   |   9
----------------------
""")
# Get the user's input to start or quit the game.
user_input = input("Press any key to play, q to quit : ")
start_game = True if user_input != "q" else False


def print_game_board():
    print(f"""
----------------------
    {game_board[0][0]}   |   {game_board[0][1]}   |   {game_board[0][2]}   
----------------------
    {game_board[1][0]}   |   {game_board[1][1]}   |   {game_board[1][2]}
----------------------
    {game_board[2][0]}   |   {game_board[2][1]}   |   {game_board[2][2]}
----------------------
    """)


def update_game_board(user_entry, tag="X"):
    global user_paces        
    global computer_paces
    if not 1 <= user_entry <= 9:
        raise ValueError("Please enter a number between 1 and 9!")
    position = game_board_position[user_entry]
    if position in user_paces or position in computer_paces:
        raise ValueError("This position is already marked!")
    (x, y) = position
    if tag == "X":  
        user_paces.append(position)
    else:
        computer_paces.append(position)
    game_board[x][y] = tag


def evaluate_game(paces):
    if len(paces) >= 3:
        for combination in winning_combination:
            correct_pace = 0
            for pace in paces:
                if pace in combination:
                    correct_pace += 1
                    if correct_pace == 3:
                        return True
    return False


def random_move():
    move = random.randint(1, 9)
    if len(user_paces + computer_paces) <= 9:
        if game_board_position[move] in user_paces + computer_paces:
            return random_move()
        else:
            return move


while start_game:
    print("You are X computer is O.")
    print_game_board()
    while True:
        user_input = input("Enter a Number: ")
        try:
            update_game_board(int(user_input))
            print_game_board()
            if evaluate_game(user_paces):
                print(user_wins)
                start_game = False
                break
            time.sleep(2)

            if len(user_paces + computer_paces) < 9:
                computer_entry = random_move()
                update_game_board(computer_entry, "O")
                print_game_board()


            if evaluate_game(computer_paces):
                print(computer_wins)
                start_game = False
                break
            elif len(user_paces + computer_paces) >= 9:
                print(draw_art)
                start_game = False
                break

        except ValueError as e:
            print(e)
            continue
print(bye_art)
