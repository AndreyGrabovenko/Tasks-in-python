from tkinter import *
from tkinter import messagebox as mb
p = 0
class Choice(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Выберите сколько нужно забрать конфет?")
        self.resizable(False, False)
        self.numbers = {
            1:'Забрать 1 конфету',
            2:'Забрать 2 конфеты',
            3:'Забрать 3 конфеты',
            4:'Забрать 4 конфеты',
            5:'Забрать 5 конфет',
            6:'Забрать 6 конфет',
            7:'Забрать 7 конфет',
            8:'Забрать 8 конфет',
            9:'Забрать 9 конфет',
            10:'Забрать 10 конфет',
            11:'Забрать 11 конфет',
            12:'Забрать 12 конфет',
            13:'Забрать 13 конфет',
            14:'Забрать 14 конфет',
            15:'Забрать 15 конфет',
            16:'Забрать 16 конфет'
        }
        self.radio_var = IntVar()
        self.radio_var.set(1)
        t = 1
        x = 1
        for key in sorted(self.numbers):
            if key == 5: t += 1
            if key == 9: t += 1
            if key == 13: t += 1
            if x >= 5 : x = 1
            Radiobutton(self, text = self.numbers[key], variable = self.radio_var, 
                            value = key).grid(column=t, row=x)
            x +=1
        self.centerWindow()
    def centerWindow(self):
        w = 530
        h = 110
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
    def play1(self):
        global p
        mb.showinfo('Выбор', 'Конфет забрано: '+ str(self.radio_var.get()))
        self.quit()
        p = self.radio_var.get()
        self.grab_focuss1()
        return p
    def quit(self):
        self.destroy()
    def grab_focuss1(self):
        self.grab_set()
        self.focus_set()
        self.wait_window()
