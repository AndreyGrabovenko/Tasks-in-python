# Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
from tkinter import *
from tkinter import messagebox
import random

root = Tk()


def on_closing():
    global root
    if messagebox.askokcancel("Выйти из приложения", "Хотите выйти из приложения?"):
        root.destroy()


CHECK_PLAYER1 = 0
CHECK_PLAYER2 = 0
CHECK_PLAYER3 = 0
SCORE = 2021
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
count1, count2, count3 = 1, 1, 0
temp1, temp2, temp3, count_lottery = 0, 0, 0, 0
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title('Игра в конфетки)')
root.resizable(False, False)
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - WINDOW_WIDTH) / 2
y = (sh - WINDOW_HEIGHT) / 2
root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, x, y))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


cs = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
            bg="red", highlightthickness=0)
cs.pack()
root.iconphoto(True, PhotoImage(file=('candy_game\iconka.png')))

obj_img = PhotoImage(file=('candy_game\landscape-games1.png'))
cs.create_image(0, 0, anchor=NW, image=obj_img)

obj_img_player1 = PhotoImage(file=('candy_game\phon.png'))
cs.create_image(38, 270, anchor=NW, image=obj_img_player1)

obj_img_player2 = PhotoImage(file=('candy_game\phon1.png'))
cs.create_image(971, 270, anchor=NW, image=obj_img_player2)

_score = cs.create_text(630, 150, text='Конфет осталось: {}'.format(
    SCORE), font=("WiGuru 2", 35), fill=rgb_to_hex((27, 36, 33)))
cs.create_text(38, 170, text='Игрок 1', font=("WiGuru 2", 26),
               fill=rgb_to_hex((35, 63, 38)), anchor=NW)
_taken_away1 = cs.create_text(38, 230, text='Конфет забрано: {}'.format(
    CHECK_PLAYER1), font=("WiGuru 2", 18), fill=rgb_to_hex((35, 63, 38)), anchor=NW)
cs.create_text(308, 270, text='Сколько забрать\nконфет?', font=(
    "WiGuru 2", 20), fill=rgb_to_hex((35, 63, 38)), anchor=NW)

_player2 = cs.create_text(971, 170, text='Игрок 2', font=(
    "WiGuru 2", 26), fill=rgb_to_hex((35, 63, 38)), anchor=NW)
_taken_away2 = cs.create_text(971, 230, text='Конфет забрано: {}'.format(
    CHECK_PLAYER2), font=("WiGuru 2", 18), fill=rgb_to_hex((35, 63, 38)), anchor=NW)
cs.create_text(710, 270, text='Сколько забрать\nконфет?', font=(
    "WiGuru 2", 20), fill=rgb_to_hex((35, 63, 38)), anchor=NW)

while True:
    def update():
        global _taken_away2, _taken_away1, _score, _player2, label_lottery
        global _won1, _won2, _won3, count1, count2, count3, CHECK_PLAYER1
        global CHECK_PLAYER2, CHECK_PLAYER3, SCORE, temp1, temp2, temp3, count_lottery
        CHECK_PLAYER1 = 0
        CHECK_PLAYER2 = 0
        CHECK_PLAYER3 = 0
        SCORE = 2021
        count1, count2, count3 = 1, 1, 0
        temp1, temp2, temp3, count_lottery = 0, 0, 0, 0
        button_player2_3.place(x=823, y=410)
        button_player2_2.place(x=911, y=350)
        button_player2.place(x=823, y=350)
        button_computer.place(x=470, y=547)
        button_lottery.place(x=550, y=460)
        label_player1["text"] = count1
        label_player2["text"] = count2
        cs.itemconfigure(_score, text='Конфет осталось: {}'.format(SCORE))
        cs.itemconfigure(
            _taken_away1, text='Конфет забрано: {}'.format(CHECK_PLAYER1))
        cs.itemconfigure(
            _taken_away2, text='Конфет забрано: {}'.format(CHECK_PLAYER2))
        cs.itemconfigure(_player2, text='Игрок 2')
        try:
            cs.delete(_won1)
        except NameError:
            t = 1
        try:
            cs.delete(_won2)
        except NameError:
            t = 1
        try:
            cs.delete(_won3)
        except NameError:
            t = 1
        try:
            label_lottery.destroy()
        except NameError:
            t = 1


    def player1_minus():
        global count1
        if count1 > 1:
            count1 -= 1
            label_player1["text"] = count1
            if count1 == 1 or count1 < 1:
                button_player1["state"] = root.DISABLED


    def player2_minus():
        global count2
        if count2 > 1:
            count2 -= 1
            label_player2["text"] = count2
            if count2 == 1 or count2 < 1:
                button_player2["state"] = root.DISABLED


    def player1_plus():
        global count1
        if count1 < 28:
            count1 += 1
            label_player1["text"] = count1
            if count1 == 1 or count1 < 1:
                button_player1_1["state"] = root.DISABLED


    def player2_plus():
        global count2
        if count2 < 28:
            count2 += 1
            label_player2["text"] = count2
        else:
            button_player2_2["state"] = root.DISABLED


    def take1():
        global _won1, count1, count3, CHECK_PLAYER1, SCORE, temp1, temp2, temp3
        if SCORE == 0:
            button_player1_3["state"] = root.DISABLED
        elif temp1 < 1:
            if SCORE - count1 > 0:
                SCORE -= count1
                CHECK_PLAYER1 += count1
                cs.itemconfigure(
                    _score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(
                    _taken_away1, text='Конфет забрано: {}'.format(CHECK_PLAYER1))
                temp1 += 1
                temp2 = 0
                temp3 = 0
            else:
                while SCORE - count1 < 0:
                    count1 -= 1
                SCORE -= count1
                CHECK_PLAYER1 += count1
                cs.itemconfigure(
                    _score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(
                    _taken_away1, text='Конфет забрано: {}'.format(CHECK_PLAYER1))
                _won1 = cs.create_text(210, 10, text='Победил игрок 1!!!', font=(
                    "WiGuru 2", 60), fill="red", anchor=NW)
            if count3 > 0:
                computer()
        else:
            button_player1_3["state"] = root.DISABLED
        if count3 > 0:
            computer()


    def take2():
        global _won2, count2, CHECK_PLAYER2, SCORE, temp1, temp2
        button_lottery.place_forget()
        button_computer.place_forget()
        try:
            label_lottery.destroy()
        except NameError:
            t = 1
        if SCORE == 0:
            button_player2_3["state"] = root.DISABLED
        elif temp2 < 1:
            if SCORE - count2 > 0:
                SCORE -= count2
                CHECK_PLAYER2 += count2
                cs.itemconfigure(
                    _score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(
                    _taken_away2, text='Конфет забрано: {}'.format(CHECK_PLAYER2))
                temp2 += 1
                temp1 = 0
            else:
                while SCORE - count2 < 0:
                    count2 -= 1
                SCORE -= count2
                CHECK_PLAYER2 += count2
                cs.itemconfigure(
                    _score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(
                    _taken_away2, text='Конфет забрано: {}'.format(CHECK_PLAYER2))
                _won2 = cs.create_text(210, 10, text='Победил игрок 2!!!', font=(
                    "WiGuru 2", 60), fill="red", anchor=NW)
        else:
            button_player2_3["state"] = root.DISABLED


    def computer():
        global _player2, _won3, count3, CHECK_PLAYER3, SCORE, temp1, temp3
        cs.itemconfigure(_player2, text='Компьютер')
        button_player2_3.place_forget()
        button_player2_2.place_forget()
        button_player2.place_forget()
        button_computer.place_forget()
        button_lottery.place_forget()
        try:
            label_lottery.destroy()
        except NameError:
            t = 1
        if temp3 < 1:
            if SCORE > 28:
                count3 = random.randint(1, 28)
                if SCORE < 100:
                    count3 = SCORE % 29
                if count3 < 1:
                    count3 += 1
                SCORE -= count3
                CHECK_PLAYER3 += count3
                label_player2["text"] = count3
                cs.itemconfigure(
                    _score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(
                    _taken_away2, text='Конфет забрано: {}'.format(CHECK_PLAYER3))
                temp3 += 1
                temp1 = 0
                count3 = 1
            else:
                while not SCORE == count3:
                    count3 += 1
                SCORE -= count3
                CHECK_PLAYER3 += count3
                cs.itemconfigure(
                    _score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(
                    _taken_away2, text='Конфет забрано: {}'.format(CHECK_PLAYER3))
                _won3 = cs.create_text(210, 10, text='Победил компьютер!!!', font=(
                    "WiGuru 2", 60), fill="red", anchor=NW)
                temp3 += 1


    def lottery():
        global label_lottery, count_lottery
        if count_lottery > 0:
            button_lottery["state"] = root.DISABLED
        elif count_lottery == 0:
            count_lottery += 1
            lottery1 = random.randint(1, 2)
            label_lottery = Label(cs, width=11, font=("WiGuru 2", 20), text=f"Ход {lottery1} игрока")
            label_lottery.place(x=560, y=410)


    button_lottery = Button(root, text='жеребьёвка', font=(
        "WiGuru 2", 20), bd=8, bg=rgb_to_hex((136, 211, 206)), command=lottery)
    button_lottery.place(x=550, y=460)

    button_player1 = Button(
        root, text='-', font=("WiGuru 2", 18), state=NORMAL, command=player1_minus)
    button_player1.place(x=308, y=350)
    label_player1 = Label(cs, width=2, font=("WiGuru 2", 29), text=count1)
    label_player1.place(x=344, y=350)
    button_player1_1 = Button(
        root, text='+', font=("WiGuru 2", 18), state=NORMAL, command=player1_plus)
    button_player1_1.place(x=399, y=350)
    button_player1_3 = Button(root, text='Забрать', font=(
        "WiGuru 2", 19), bg=rgb_to_hex((41, 50, 60)), foreground=rgb_to_hex((190, 215, 203)), command=take1)
    button_player1_3.place(x=308, y=410)

    button_player2 = Button(
        root, text='-', font=("WiGuru 2", 18), command=player2_minus)
    button_player2.place(x=823, y=350)
    label_player2 = Label(cs, width=2, font=("WiGuru 2", 29), text=count2)
    label_player2.place(x=857, y=350)
    button_player2_2 = Button(
        root, text='+', font=("WiGuru 2", 18), command=player2_plus)
    button_player2_2.place(x=911, y=350)
    button_player2_3 = Button(root, text='Забрать', font=(
        "WiGuru 2", 19), bg=rgb_to_hex((41, 50, 60)), foreground=rgb_to_hex((190, 215, 203)), command=take2)
    button_player2_3.place(x=823, y=410)

    button_computer = Button(root, text='Играть с компьютером?', font=(
        "WiGuru 2", 19), bd=8, bg=rgb_to_hex((151, 149, 240)), command=computer)
    button_computer.place(x=470, y=547)

    button_player_update3 = Button(root, text='Обновить?', font=(
        "WiGuru 2", 20), bd=8, bg=rgb_to_hex((136, 211, 206)), command=update)
    button_player_update3.place(x=550, y=630)
    root.mainloop()
