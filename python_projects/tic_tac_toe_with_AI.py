import math
board=[' ' for _ in range(9)]
def print_board():
    i=0
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('  |  ' .join(row))
        i+=1
        if  i != 3:
            print("_____________\n")
        else:print("\n")

def is_winner(board, player):
    winner_positions=[
       [0,1,2],[3,4,5],[6,7,8],
       [0,3,6],[1,4,7],[2,5,8],
       [0,4,8],[2,4,6]
    ]
    return any( all(board[i]==player for i in pos)for pos in winner_positions)
def empty_cells():
    return [i for i, val in enumerate(board) if val == ' ']
 
def mimimax(is_maximizing):
    if is_winner(board,'O'):
        return +1
    elif is_winner(board,'X'):
        return -1
    elif not empty_cells():
        return 0

    if is_maximizing:
        best=-math.inf
        for i in empty_cells():
            board[i]='O'
            score=mimimax(False)
            board[i]=' '
            best=max(score,best)
        return best
    else:
        best=math.inf
        for i in empty_cells():
            board[i]='X'
            score=mimimax(True)
            board[i]=' '
            best=min(score,best)
        return best

def ai_move():
    best=-math.inf
    move=None
    for i in empty_cells():
        board[i]='O'
        score=mimimax(False)
        board[i]=' '
        if score>best:
            best=score
            move=i
    board[move]='O'

def play_game():
    print("X is you and O is AI")
    print_board()
    while True:
        try:
            move=int(input("Enter your move (0-8): "))
            if board[move]!=' ':
                print("spot taken!")
                continue
            board[move]='X'
        except(IndexError,ValueError):
            print("Invalid move")
            continue
        print_board()
        if is_winner(board,'X'):
            print_board()
            print("Congratulations You Win!")
            break
        if ' ' not in board:
            print("Draw!")
            break
        ai_move()
        print_board()
        if is_winner(board,'O'):
            print_board()
            print("AI Wins!")
            break
        if ' ' not in board:
            print("Draw!")
            break
        
print("Welcome to Tic Tac Toe!")
input("Press Enter to play")
play_game()
            
        
    

