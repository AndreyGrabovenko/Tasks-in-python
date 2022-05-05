# Помните игру с конфетами из модуля "Математика и Информатика"? 
# Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
from tkinter import *
from tkinter import messagebox

temp = 0
root = Tk()

def on_closing():
    global root
    if messagebox.askokcancel("Выйти из приложения", "Хотите выйти из приложения?"):
        root.destroy()

def update():
    global root,temp
    temp +=1
    root.destroy()
    game()

def game():
    global temp, root
    if temp > 0:
        root = Tk()
    CHECK_PLAYER1 = 0
    CHECK_PLAYER2 = 0
    CHECK_PLAYER3 = 0
    SCORE = 250
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720
    count1, count2, count3 = 1, 1, 0
    temp1, temp2, temp3 = 0, 0, 0
    
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
    
    cs = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="red", highlightthickness=0)
    cs.pack()
    root.iconphoto(True, PhotoImage(file=('candy_game\iconka.png')))
    
    obj_img = PhotoImage(file=('candy_game\landscape-games1.png'))
    cs.create_image(0,0, anchor=NW, image = obj_img)
    
    obj_img_player1 = PhotoImage(file=('candy_game\phon.png'))
    cs.create_image(100,400, anchor=NW, image = obj_img_player1)
    
    obj_img_player2 = PhotoImage(file=('candy_game\phon1.png'))
    cs.create_image(935,400, anchor=NW, image = obj_img_player2)
    
    _score = cs.create_text(480, 300, text='Конфет осталось: {}'.format(SCORE), font=("WiGuru 2", 20), fill="red", anchor=NW)
    cs.create_text(170, 356, text='Игрок 1', font=("WiGuru 2", 24), fill="red", anchor=NW)
    _taken_away1 = cs.create_text(100, 50, text='Конфет забрано: {}'.format(CHECK_PLAYER1), font=("WiGuru 2", 20), fill="red", anchor=NW)
    cs.create_text(60, 180, text='Сколько забрать конфет?', font=("WiGuru 2", 20), fill="red", anchor=NW)
    
    _player2 = cs.create_text(1005, 356, text='Игрок 2', font=("WiGuru 2", 24), fill="red", anchor=NW)
    _taken_away2 = cs.create_text(935, 50, text='Конфет забрано: {}'.format(CHECK_PLAYER2), font=("WiGuru 2", 20), fill="red", anchor=NW)
    cs.create_text(895, 180, text='Сколько забрать конфет?', font=("WiGuru 2", 20), fill="red", anchor=NW)
    
    def player1_minus():
        nonlocal count1
        if count1 > 1:
            count1 -= 1
            label_player1["text"] = count1
            if count1 == 1 or count1 < 1:
                button_player1["state"] = root.DISABLED
    def player2_minus():
        nonlocal count2
        if count2 > 1:
            count2 -= 1
            label_player2["text"] = count2
            if count2 == 1 or count2 < 1:
                button_player2["state"] = root.DISABLED
    def player1_plus():
        nonlocal count1
        if count1 < 28:
            count1 += 1
            label_player1["text"] = count1
            if count1 == 1 or count1 < 1:
                button_player1_1["state"] = root.DISABLED
    def player2_plus():
        nonlocal count2
        if count2 < 28:
            count2 += 1
            label_player2["text"] = count2
        else:
            button_player2_2["state"] = root.DISABLED
    def take1():
        nonlocal count1, SCORE, CHECK_PLAYER1, temp1, temp2, temp3, computer
        if SCORE == 0:
            button_player1_3["state"] = root.DISABLED
        elif temp1 < 1:
            if SCORE - count1 > 0:
                SCORE -= count1
                CHECK_PLAYER1 += count1
                cs.itemconfigure(_score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(_taken_away1, text='Конфет забрано: {}'.format(CHECK_PLAYER1))
                temp1 += 1
                temp2 = 0
                temp3 = 0
            else:
                while SCORE - count1 < 0:
                    count1 -=1
                SCORE -= count1
                CHECK_PLAYER1 += count1
                cs.itemconfigure(_score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(_taken_away1, text='Конфет забрано: {}'.format(CHECK_PLAYER1))
                cs.create_text(300, 80, text='Победил игрок 1!!!', font=("WiGuru 2", 60), fill="red", anchor=NW)
                button_player_update = Button(root, text = 'Обновить?', font = ("WiGuru 2", 40), bg='red', command= update)
                button_player_update.place(x= 470, y= 220)
            if count3 > 0:
                computer()
        else:
            button_player1_3["state"] = root.DISABLED
        if count3 > 0:
            computer()
    def take2():
        nonlocal count2, SCORE, CHECK_PLAYER2, temp1, temp2
        if SCORE == 0:
            button_player2_3["state"] = root.DISABLED
        elif temp2 < 1:
            if SCORE - count2 >= 0:
                SCORE -= count2
                CHECK_PLAYER2 += count2
                cs.itemconfigure(_score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(_taken_away2, text='Конфет забрано: {}'.format(CHECK_PLAYER2))
                # button_player1_3["state"] = root.DISABLED
                temp2 += 1
                temp1 = 0
            else:
                while SCORE - count2 < 0:
                    count2 -=1
                SCORE -= count2
                CHECK_PLAYER2 += count2
                cs.itemconfigure(_score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(_taken_away2, text='Конфет забрано: {}'.format(CHECK_PLAYER2))
                cs.create_text(300, 80, text='Победил игрок 2!!!', font=("WiGuru 2", 60), fill="red", anchor=NW)
                button_player_update = Button(root, text = 'Обновить?', font = ("WiGuru 2", 40), bg='red', command= update)
                button_player_update.place(x= 470, y= 220)
        else:
            button_player2_3["state"] = root.DISABLED
    def computer():
        nonlocal count3, SCORE, CHECK_PLAYER3, temp1, temp3
        cs.delete(_player2)
        cs.create_text(980, 356, text="Компьютер", font=("WiGuru 2", 24), fill="red", anchor=NW)
        button_player2_3.place_forget()
        button_player2_2.place_forget()
        button_player2.place_forget()
        button_player.place_forget()
        if temp3 < 1:
            if SCORE > 29:
                count3 = SCORE % 29
                if count3 == 0:
                    count3 +=1
                SCORE -= count3
                CHECK_PLAYER3 += count3
                label_player2["text"] = count3
                cs.itemconfigure(_score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(_taken_away2, text='Конфет забрано: {}'.format(CHECK_PLAYER3))
                temp3 += 1
                temp1 = 0
                count3 = 1
            else:
                while not SCORE == count3:
                    count3 +=1
                SCORE -= count3
                CHECK_PLAYER3 += count3
                cs.itemconfigure(_score, text='Конфет осталось: {}'.format(SCORE))
                cs.itemconfigure(_taken_away2, text='Конфет забрано: {}'.format(CHECK_PLAYER3))
                cs.create_text(180, 80, text='Победил компьютер!!!', font=("WiGuru 2", 60), fill="red", anchor=NW)
                button_player_update = Button(root, text = 'Обновить?', font = ("WiGuru 2", 40), bg='red', command= update)
                button_player_update.place(x= 470, y= 220)
                temp3 += 1
    
    button_player1 = Button(root, text = '-', font = ("WiGuru 2", 18), state = NORMAL, command= player1_minus)
    button_player1.place(x= 171, y= 230)
    label_player1 = Label(cs, width = 2, font =("WiGuru 2", 29), text = count1)
    label_player1.place(x=204, y=230)
    button_player1_1 = Button(root, text = '+', font = ("WiGuru 2", 18), state = NORMAL, command= player1_plus)
    button_player1_1.place(x= 260, y= 230)
    button_player1_3 = Button(root, text = 'Забрать', font = ("WiGuru 2", 19), command= take1)
    button_player1_3.place(x= 171, y= 289)
    
    button_player2 = Button(root, text = '-', font = ("WiGuru 2", 18), command= player2_minus)
    button_player2.place(x= 1006, y= 230)
    label_player2 = Label(cs, width = 2, font =("WiGuru 2", 29), text = count2)
    label_player2.place(x=1039, y=230)
    button_player2_2 = Button(root, text = '+', font = ("WiGuru 2", 18), command= player2_plus)
    button_player2_2.place(x= 1095, y= 230)
    button_player2_3 = Button(root, text = 'Забрать', font = ("WiGuru 2", 19), command= take2)
    button_player2_3.place(x= 1006, y= 289)
    
    button_player = Button(root, text = 'Играть с компьютером?', font = ("WiGuru 2", 19), bg='red', command= computer)
    button_player.place(x= 470, y= 620)
    root.mainloop()
game()