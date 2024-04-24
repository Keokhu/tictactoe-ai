import sys

# The game board is represented as a 3x3 list of lists
board = [[' ' for _ in range(3)] for _ in range(3)]

# The AI player is 'X' and the human player is 'O'
ai_player = 'X'
human_player = 'O'

# The minimax algorithm takes the current board and depth as input
def minimax(board, depth, maximizing_player):
    if check_win(board, human_player):
        return -1
    elif check_win(board, ai_player):
        return 1
    elif not any(any(cell != ' ' for cell in row) for row in board):
        return 0
    
    if maximizing_player:
        max_eval = -sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ai_player
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = human_player
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# The function to check if a player has won
def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# The function to get the best move for the AI player
def get_best_move():
    best_score = -sys.maxsize
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = ai_player
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = ai_player
    return move

# The function to print the game board
def print_board():
    for row in board:
        print('|'.join(row))
        print('-----')

# The main function to play the game
def main():
    print("Tic-Tac-Toe")
    print_board()
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column separated by a space): ").split())
            if board[row - 1][col - 1] == ' ':
                board[row - 1][col - 1] = human_player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")
        except IndexError:
            print("Invalid row or column. Try again.")
    while not check_win(board, ai_player) and not check_win(board, human_player) and any(any(cell != ' ' for cell in row) for row in board):
        move = get_best_move()
        board[move[0]][move[1]] = ai_player
        print_board()
        if check_win(board, ai_player):
            print("AI wins!")
            sys.exit()
        elif not any(any(cell != ' ' for cell in row) for row in board):
            print("It's a draw!")
            sys.exit()
        row, col = map(int, input("Enter your move (row and column separated by a space): ").split())
        if board[row - 1][col - 1] == ' ':
            board[row - 1][col - 1] = human_player
        else:
            print("Invalid move. Try again.")
        if check_win(board, human_player):
            print("You win!")
            sys.exit()

if __name__ == "__main__":
    main()