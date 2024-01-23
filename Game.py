# Function to make a move
def make_move(player):
    valid_move = False
    while not valid_move:
        move = input() # input will range from 0-8
        if board[int(move)] == ' ':
            board[int(move)] = player
            valid_move = True

def check_win(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for j in win_conditions:
        if board[j[0]] == board[j[1]] == board[j[2]] == player:
            return True
    return False
  
def game():
    for i in range(9):
        current_player = 'X' if i % 2 == 0 else 'O'
        make_move(current_player)
        if check_win(current_player):
            print(current_player + " wins!")
            return
    print("It's a draw!")

# Start the game
game()
