# Initialize Tic Tac Toe board
board = [' ' for _ in range(9)]

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def is_draw(board):
    return ' ' not in board


def player_move(board):
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")


def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def ai_best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = 'O'


# ---- Main Game Loop ----
while True:
    print_board(board)
    player_move(board)
    if check_winner(board, 'X'):
        print_board(board)
        print("🎉 You win!")
        break
    if is_draw(board):
        print_board(board)
        print("🤝 Draw!")
        break

    ai_best_move(board)
    if check_winner(board, 'O'):
        print_board(board)
        print("💻 AI wins!")
        break
    if is_draw(board):
        print_board(board)
        print("🤝 Draw!")
        break
