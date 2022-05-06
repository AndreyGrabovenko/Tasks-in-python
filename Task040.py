# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

from tkinter import *
from tkinter import messagebox
import random

game_run = True
field = []
cross_count = 0

def on_closing():
    global root
    if messagebox.askokcancel("Выйти из приложения", "Хотите выйти из приложения?"):
        root.destroy()

root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title('Игра в крестики нолики')
root.resizable(False, False)
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - 416) / 2
y = (sh - 570) / 2
root.geometry('%dx%d+%d+%d' % (405, 570, x, y))
butt = Frame(root)
lebel = Label( width= 20, text="Игра в крестики нолики", font=("WiGuru 2", 20))
lebel.place(x=35, y=0)

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'green'
    global game_run, cross_count
    game_run = True
    cross_count = 0

def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')

def check_win(cmb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], cmb)
        check_line(field[0][n], field[1][n], field[2][n], cmb)
    check_line(field[0][0], field[1][1], field[2][2], cmb)
    check_line(field[2][0], field[1][1], field[0][2], cmb)

def check_line(a1, a2, a3, cmb):
    if a1['text'] == cmb and a2['text'] == cmb and a3['text'] == cmb:
        a1['background'] = a2['background'] = a3['background'] = 'gold'
        global game_run
        game_run = False

def can_win(a1, a2, a3, cmb):
    res = False
    if a1['text'] == cmb and a2['text'] == cmb and a3['text'] == " ":
        a3['text'] = 'O'
        res = True
    if a1['text'] == cmb and a2['text'] == " " and a3['text'] == cmb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == " " and a2['text'] == cmb and a3['text'] == cmb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], "O"):
            return
        if can_win(field[0][n], field[1][n], field[2][n], "O"):
            return
    if can_win(field[0][0], field[1][1], field[2][2], "O"):
        return
    if can_win(field[2][0], field[1][1], field[0][2], "O"):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], "X"):
            return
        if can_win(field[0][n], field[1][n], field[2][n], "X"):
            return
    if can_win(field[0][0], field[1][1], field[2][2], "X"):
        return
    if can_win(field[2][0], field[1][1], field[0][2], "X"):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == " ":
            field[row][col]['text'] = "O"
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(butt, width=5, height=2, text=" ", font=(
            "WiGuru 2", 30), background='green', command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky= "nsew")
        line.append(button)
    field.append(line)
butt.place(x=0, y=45, anchor=NW)
new_button = Button(root, width=24, text="new game", font = ("WiGuru 2", 20), bg='blue', command=new_game)
new_button.place(x=0, y=508)

root.mainloop()