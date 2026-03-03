import tkinter as tk
from tkinter import messagebox
from random import randrange


def create_board():
    return [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

board = create_board()
buttons = []
game_over = False


def draw_board():
    for i in range(3):
        for j in range(3):
            value = board[i][j]

            if value in ['X', 'O']:
                buttons[i][j]["text"] = value
                buttons[i][j]["state"] = "disabled"


def check_winner():

    # Linhas
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    # Colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Diagonais
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    # Empate
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return None

    return "Empate"



def computer_move():
    global game_over

    if game_over:
        return

    free_positions = []

    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free_positions.append((i, j))

    if free_positions:
        pos = free_positions[randrange(len(free_positions))]
        board[pos[0]][pos[1]] = 'X'

    draw_board()
    check_game_end()


def player_move(row, col):
    global game_over

    if game_over:
        return

    if board[row][col] not in ['X', 'O']:
        board[row][col] = 'O'

    draw_board()
    check_game_end()

    if not game_over:
        window.after(500, computer_move)



def check_game_end():
    global game_over

    result = check_winner()

    if result == 'X':
        messagebox.showinfo("Fim de Jogo", "Computador venceu!")
        game_over = True

    elif result == 'O':
        messagebox.showinfo("Fim de Jogo", "Você venceu!")
        game_over = True

    elif result == "Empate":
        messagebox.showinfo("Fim de Jogo", "Empate!")
        game_over = True


window = tk.Tk()
window.title("Jogo da Velha")

for i in range(3):
    row_buttons = []
    for j in range(3):
        btn = tk.Button(
            window,
            text="",
            font=("Arial", 24),
            width=5,
            height=2,
            command=lambda r=i, c=j: player_move(r, c)
        )
        btn.grid(row=i, column=j)
        row_buttons.append(btn)

    buttons.append(row_buttons)



board[1][1] = 'X'
draw_board()

window.mainloop()