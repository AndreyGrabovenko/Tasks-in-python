# Помните игру с конфетами из модуля "Математика и Информатика"? 
# Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

from logging import root
from math import remainder
from tkinter import *
from candy_game import *
from tkinter import messagebox
from PIL import Image, ImageTk



CHECK_PLAYER1 = 0
CHECK_PLAYER2 = 0
SCORE = 1000
amount4 = 0
class candy(Tk):
    def __init__(self):
        super().__init__()
        WINDOW_WIDTH = 1280
        WINDOW_HEIGHT = 720
        def on_closing():
            if messagebox.askokcancel("Выйти из приложения", "Хотите выйти из приложения?"):
                self.destroy()
        
        self.protocol("WM_DELETE_WINDOW", on_closing)
        self.title('Игра в конфетки)')
        self.resizable(False, False)
        canvas = Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        canvas.pack()
        self.iconphoto(True, PhotoImage(file=('candy_game\iconka.png')))
        
        
        our_image = Image.open('candy_game\landscape-games1.png')
        our_image = ImageTk.PhotoImage(our_image)
        our_label = Label(image = our_image)
        our_label.image = our_image
        our_label.place(x = 0, y = 0)
        
        our_image1 = Image.open('candy_game\phon.jpg')
        our_image1 = our_image1.resize((300,300), Image.ANTIALIAS)
        our_image1 = ImageTk.PhotoImage(our_image1)
        our_label1 = Label(image = our_image1)
        our_label1.image = our_image1
        our_label1.place(x = 100, y = 350)
        
        our_image2 = Image.open('candy_game\phon1.jpg')
        our_image2 = our_image2.resize((300,300), Image.ANTIALIAS)
        our_image2 = ImageTk.PhotoImage(our_image2)
        our_label2 = Label(image = our_image2)
        our_label2.image = our_image2
        our_label2.place(x = 870, y = 350)
        def test():
            global SCORE, CHECK_PLAYER1, CHECK_PLAYER2, amount4
            label_score = Label(self, text='Конфет осталось: {}'.format(SCORE), font = ('Arial', 20))
            label_score.pack()
            label_score.place(relx=0.5, rely=0.3, anchor=CENTER)

            label_player1 = Label(self, text = 'Игрок 1', font = ('Times', 40))
            label_player1.pack()
            label_player1.place(relx=0.2, rely=0.43, anchor=CENTER)
            
            label_player2 = Label(self, text = 'Игрок 2', font = ('Times', 40))
            label_player2.pack()
            label_player2.place(relx=0.8, rely=0.43, anchor=CENTER)
            
            check_player1 = Label(self, text='Конфет забрано: {}'.format(CHECK_PLAYER1), font = ('Arial', 20))
            check_player1.pack()
            check_player1.place(relx=0.2, rely=0.1, anchor=CENTER)
            
            
            check_player3 = Label(self, text='Сколько забрать конфет? ', font = ('Arial', 15))
            check_player3.pack()
            check_player3.place(relx=0.8, rely=0.25, anchor=CENTER)
            
            # def www():
            #     nonlocal label_score
            #     label_score.destroy()
            #     label_score = Label(self, text='Конфет осталось: {}'.format(o()), font = ('Arial', 20))
            #     label_score.pack()
            #     label_score.place(relx=0.5, rely=0.3, anchor=CENTER)
            amount1 = Entry(width = 5, font =('Arial', 20))
            amount1.pack()
            amount1.place(relx=0.2, rely=0.3, anchor=CENTER)
            # button_player1 = Button(self, text = 'Забрать?', command = result, font = ('Arial', 15))
            # button_player1.pack()
            # button_player1.place(relx=0.2, rely=0.3, anchor=CENTER)
            
            check_player2 = Label(self, text='Конфет забрано: {}'.format(CHECK_PLAYER2), font = ('Arial', 20))
            check_player2.pack()
            check_player2.place(relx=0.8, rely=0.1, anchor=CENTER)
            amount2 = Entry(width = 5, font =('Arial', 20))
            amount2.pack()
            amount2.place(relx=0.8, rely=0.3, anchor=CENTER)
            amount4 = amount2.get()
            button_player2 = Button(self, text = 'Забрать?', command = result, font = ('Arial', 15))
            button_player2.pack()
            button_player2.place(relx=0.8, rely=0.356, anchor=CENTER)
        test()
def result():
    winner()
    global SCORE, CHECK_PLAYER1, CHECK_PLAYER2, amount4
    while True:
        try:
            temp =int(amount4)
        except ValueError:
            mb.showinfo('число введено не верно!')
            amount2 = Entry(width = 5, font =('Arial', 20))
            amount2.pack()
            amount2.place(relx=0.8, rely=0.3, anchor=CENTER)
            amount4 = amount2.get()
        else:
            break
    if temp <= 28:
        if SCORE - temp != 0:
            SCORE -= temp
        else:
            while True:
                try:
                    mb.showinfo('Это слишком много!')
                    amount2 = Entry(width = 5, font =('Arial', 20))
                    amount2.pack()
                    amount2.place(relx=0.8, rely=0.3, anchor=CENTER)
                    amount4 = amount2.get()
                    temp =int(amount4)
                except ValueError:
                    mb.showinfo('число введено не верно!')
                    amount2 = Entry(width = 5, font =('Arial', 20))
                    amount2.pack()
                    amount2.place(relx=0.8, rely=0.3, anchor=CENTER)
                    amount4 = amount2.get()
                else:
                    break
def winner():
    global SCORE, CHECK_PLAYER1, CHECK_PLAYER2, amount4
    if SCORE == 0:
        if CHECK_PLAYER1 < CHECK_PLAYER2:
            mb.showinfo('ПОБЕДИЛ ИГРОК 2! \n И ЗАБРАЛ КОНФЕТ: ' + str(CHECK_PLAYER2))
        else:
            mb.showinfo('ПОБЕДИЛ ИГРОК 1! \n И ЗАБРАЛ КОНФЕТ: ' + str(CHECK_PLAYER1))
        SCORE = 1000
        CHECK_PLAYER1 = 0
        CHECK_PLAYER2 = 0
def f():
    global g
    g = Choice()
def main():
    apllication = candy()
    apllication.mainloop()

if __name__ == '__main__':
    main()