from tkinter import *

root = Tk()
game_still_going = True
winner = None
player = 'X'
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
robot = False

def start():
    body(root)

def setboard():
    global board, game_still_going,player
    board = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]
    game_still_going = True 
    player="X"

def creat_new(r):
    global root
    setboard()
    root = Tk()
    body(root)
    root.mainloop()

def block():
    b1, b2, b3, b4, b5, b6, b7, b8, b9 = body(root)
    for btn in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        btn["state"] = "disabled"
def enable():
    b1, b2, b3, b4, b5, b6, b7, b8, b9 = body(root)
    for btn in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        btn["state"] = "normal"

def check_if_game_over():
    global root
    check_for_winner()
    check_for_tie()
    if not game_still_going:
        block()
        y = Label(root, text=str(winner) + ' is the winner')
        y.grid(row=5, column=1)
        root.mainloop()

def check_for_winner():
    global winner, game_still_going
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    if winner:
        game_still_going = False

def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return None

def check_columns():
    global game_still_going
    col1 = board[0] == board[3] == board[6] != "_"
    col2 = board[1] == board[4] == board[7] != "_"
    col3 = board[2] == board[5] == board[8] != "_"
    if col1 or col2 or col3:
        game_still_going = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return None

def check_diagonals():
    global game_still_going
    diag1 = board[0] == board[4] == board[8] != "_"
    diag2 = board[2] == board[4] == board[6] != "_"
    if diag1 or diag2:
        game_still_going = False
    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    return None

def check_for_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False

def flip_player():
    global player
    player = 'O' if player == 'X' else 'X'

def evaluate(board):
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] != '_':
            return 1 if board[i] == 'O' else -1
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != '_':
            return 1 if board[i] == 'O' else -1
    if board[0] == board[4] == board[8] != '_':
        return 1 if board[0] == 'O' else -1
    if board[2] == board[4] == board[6] != '_':
        return 1 if board[2] == 'O' else -1
    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 1 or score == -1 or "_" not in board:
        return score

    if is_maximizing:
        best_score = -float('inf')
        for i in range(len(board)):
            if board[i] == "_":
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = "_"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(len(board)):
            if board[i] == "_":
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = "_"
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -float('inf')
    move = 0
    for i in range(len(board)):
        if board[i] == "_":
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = "_"
            if score > best_score:
                best_score = score
                move = i
    return move

def btn_click(b, index,l1):
    global player, board
    if board[index] == "_" and game_still_going:
        board[index] = player
        b["text"] = player
        check_if_game_over()
        flip_player()

        if player == 'O' and ai_active:
            ai_index = best_move()
            board[ai_index] = 'O'
            b1, b2, b3, b4, b5, b6, b7, b8, b9 = body(root)
            buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
            buttons[ai_index]["text"] = 'O'
            check_if_game_over()
            flip_player()
        
        l1["text"] = "Player: " + player

def distroy(root):
    root.destroy()
    creat_new(root)

def body(root):
    l1 = Label(root, text="Player: " + player, font=('helvetica', 20))
    b1 = Button(root, text=board[0], font=('helvetica', 20), height=3, width=6, fg='black', command=lambda: btn_click(b1, 0,l1))
    b2 = Button(root, text=board[1], font=('helvetica', 20), height=3, width=6, fg='black', command=lambda: btn_click(b2, 1,l1))
    b3 = Button(root, text=board[2], font=('helvetica', 20), height=3, width=6, fg='black', command=lambda: btn_click(b3, 2,l1))
    b4 = Button(root, text=board[3], font=('helvetica', 20), height=3, width=6, fg='black', command=lambda: btn_click(b4, 3,l1))
    b5 = Button(root, text=board[4], font=('helvetica', 20), height=3, width=6, fg='black', command=lambda: btn_click(b5, 4,l1))
    b6 = Button(root, text=board[5], font=('helvetica', 20), height=3, width=6, fg='black', command=lambda: btn_click(b6, 5,l1))
    b7 = Button(root, text=board[6], font=('helvetica', 20), height=3, width=6, fg='black', command=lambda: btn_click(b7, 6,l1))
    b8 = Button(root, text=board[7], font=('helvetica', 20), height=3, width=6, fg='black', command=lambda: btn_click(b8, 7,l1))
    b9 = Button(root, text=board[8], font=('helvetica', 20), height=3, width=6, fg='black', command=lambda: btn_click(b9, 8,l1))
    ex = Button(root, text='reset', font=('helvetica', 20), command=lambda: distroy(root))

    options_list = ["1v1", "Ai"]
    val_inside = StringVar(root)
    o = OptionMenu(root, val_inside, *options_list, command=update_player_mode)

    l1.grid(row=0, column=1)
    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)
    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)
    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)
    ex.grid(row=4, column=1)
    o.grid(row=5, column=0)

    return b1, b2, b3, b4, b5, b6, b7, b8, b9

def update_player_mode(selection):
    global ai_active
    if selection == "Ai":
        ai_active = True
    else:
        ai_active = False

ai_active = False
start()
root.mainloop()
