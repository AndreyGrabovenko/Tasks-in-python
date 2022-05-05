from random import randrange, choice
from tkinter import *
from tkinter import messagebox
from copy import deepcopy
import time

W, H = 13, 28
TILE = 25
GAME_RES = W * TILE, H * TILE
RES = 590, 740
FPS = 60
fig = []
fig2 = []
V = 3000

def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        app_running = False
        tk.destroy()

tk = Tk()
app_running = True
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Tetris")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
sw = tk.winfo_screenwidth()
sh = tk.winfo_screenheight()
x = (sw - RES[0]) / 2
y = (sh - RES[1]) / 2
tk.geometry('%dx%d+%d+%d' % (RES[0], RES[1], x, y))

sc = Canvas(tk, width=RES[0], height=RES[1], bg="red", highlightthickness=0)
sc.pack()

def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')
        return '0'

def set_record(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))

game_sc = Canvas(tk, width=W * TILE+1, height=H * TILE +
                 1, bg="yellow", highlightthickness=-1)
game_sc.place(x=20, y=20, anchor=NW)

img_obj1 = PhotoImage(file="b2.png")
sc.create_image(0, 0, anchor=NW, image=img_obj1)

img_obj2 = PhotoImage(file="b3.png")
game_sc.create_image(0, 0, anchor=NW, image=img_obj2)

grid = [game_sc.create_rectangle(
    x * TILE, y * TILE, x * TILE+TILE, y * TILE+TILE) for x in range(W) for y in range(H)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures_pos1 = [[(-1, 0), (-2, 0), (0, 0), (1, 0), (2, 0)],
                [(-1, 0), (-2, 0), (0, 0), (1, 0), (2, 0)],
                [(-1, 0), (-2, 0), (0, 0), (1, 0), (2, 0)],
                [(0, -1), (-1, -1), (-1, 0), (0, 0), (0, 1)],
                [(0, -1), (-1, -1), (-1, 0), (0, 0), (-1, 1)],
                [(-1, 0), (-1, 1), (0, 0), (0, -1), (-2, 1)],
                [(0, 0), (0, -1), (0, 1), (-1, -1), (0, 2)],
                [(0, 0), (0, -1), (0, 1), (1, -1), (0, 2)],
                [(0, 0), (0, -1), (0, 1), (1, -1), (0, -2)],
                [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 1)],
                [(0, 0), (0, -1), (1, -1), (0, 1), (1, 1)],
                [(0, 0), (0, 1), (0, 2), (-1, 0), (-2, 0)],
                [(0, 0), (1, 0), (-1, 0), (0, -1), (0, -2)],
                [(0, 0), (1, 0), (2, 0), (0, -1), (-1, -1)]]

figures_pos2 = [[(0, 0), (-1, 0), (-2, 0), (1, 0), (2, 0), (3, 0)],
                [(0, 0), (-1, 0), (-2, 0), (1, 0), (2, 0), (3, 0)],
                [(0, 0), (-1, 0), (-2, 0), (1, 0), (2, 0), (3, 0)],
                [(0, 0), (-1, -1), (-1, 0), (0, -1), (0, 1), (0, 2)],
                [(0, 0), (-1, 0), (0, 1), (-1, -1), (-2, -1), (1, 1)],
                [(0, 0), (0, -1), (0, 1), (1, -1), (0, 2), (0, 3)],
                [(0, 0), (0, -1), (0, 1), (-1, -1), (0, 2), (0, 3)],
                [(0, 0), (1, 0), (0, 1), (-1, 0), (-2, 0), (-3, 0)],
                [(0, 0), (1, 0), (2, 0), (0, 1), (-1, 0), (-2, 0)],
                [(0, 0), (1, 0), (1, 1), (2, 1), (-1, 0), (-2, 0)],
                [(0, 0), (1, 0), (1, 1), (-1, 0), (-1, 1), (-2, 0)],
                [(0, 0), (1, 0), (1, 1), (-1, 0), (-2, 0), (-2, 1)],
                [(0, 0), (1, 0), (0, 1), (-1, 0), (-1, 1), (-2, 0)],
                [(0, 0), (0, 1), (0, 2), (-1, 0), (-2, 0), (-3, 0)],
                [(0, 0), (1, 0), (0, 1), (0, 2), (-1, 0), (-2, 0)],
                [(0, 0), (0, -1), (0, 1), (-1, 0), (-2, 0), (-3, 0)],
                [(0, 0), (0, -1), (1, 0), (1, 1), (-1, 0), (-2, 0)],
                [(0, 0), (1, 0), (1, 1), (-1, 0), (-1, -1), (-2, 0)],
                [(0, 0), (1, 0), (1, 1), (-1, 0), (-2, 0), (-1, -1)],
                [(0, 0), (1, 0), (0, 1), (-1, 0), (-1, -1), (-2, 0)],
                [(0, 0), (1, 0), (0, -1), (0, 1), (-1, 0), (-2, 0)],
                [(0, 0), (0, 1), (1, 1), (0, 2), (-1, 0), (-2, 0)],
                [(0, 0), (0, 1), (1, 1), (-1, 0), (-2, 0), (-2, 1)],
                [(0, 0), (0, 1), (1, 1), (2, 1), (-1, 0), (-2, 0)],
                [(0, 0), (0, 1), (1, 1), (-1, 0), (-1, 1), (-2, 0)],
                [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 0), (-1, 1)],
                [(0, 0), (0, -1), (0, 1), (1, 1), (-1, 0), (-2, 0)],
                [(0, 0), (0, -1), (0, 1), (-1, 0), (-1, 1), (-2, 0)],
                [(0, 0), (0, 1), (1, 1), (-1, 0), (-1, -1), (-2, 0)],
                [(0, 0), (0, 1), (0, 2), (1, 1), (-1, 0), (-2, 0)],
                [(0, 0), (0, 1), (1, 1), (1, 2), (-1, 0), (-2, 0)],
                [(0, 0), (0, 1), (0, 2), (-1, 2), (-1, 0), (-2, 0)],
                [(0, 0), (1, 0), (0, 1), (0, 2), (1, 2), (-1, 0)],
                [(0, 0), (0, 1), (1, 1), (0, -1), (1, -1), (-1, 0)],
                [(0, 0), (1, 0), (1, 1), (-1, 0), (-1, -1), (-2, -1)],
                [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (1, 1)],
                [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
                [(0, 0), (0, 1), (0, 2), (1, 2), (-1, 0), (-1, 1)],
                [(0, 0), (0, 1), (1, 1), (-1, 0), (-1, -1), (-2, -1)]]

def levell(num):
    global fig, fig2, figure, number_level, figures, score
    if num == 1:
        number_level = 4
        level = {4: figures_pos, 5: figures_pos1, 6: figures_pos2}
        figures = [[[x + W // 2, y + 1, 1, 1] for x, y in fig_pos]
                   for fig_pos in level[number_level]]
        x()
        for id_fig in fig:
            game_sc.delete(id_fig)
        for id_fig in fig2:
            sc.delete(id_fig)
        score = 0
        game()
    if num == 2:
        number_level = 5
        level = {4: figures_pos, 5: figures_pos1, 6: figures_pos2}
        figures = [[[x + W // 2, y + 1, 1, 1] for x, y in fig_pos]
                   for fig_pos in level[number_level]]
        x()
        for id_fig in fig:
            game_sc.delete(id_fig)
        for id_fig in fig2:
            sc.delete(id_fig)
        score = 0
        game()
    if num == 3:
        number_level = 6
        level = {4: figures_pos, 5: figures_pos1, 6: figures_pos2}
        figures = [[[x + W // 2, y + 1, 1, 1] for x, y in fig_pos]
                   for fig_pos in level[number_level]]
        x()
        for id_fig in fig:
            game_sc.delete(id_fig)
        for id_fig in fig2:
            sc.delete(id_fig)
        score = 0
        game()

def x():
    global figures, field, figure, next_figure
    field = [[0 for i in range(W)] for j in range(H)]
    figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))

def get_color(): return (randrange(0, 100), randrange(0, 100), randrange(0, 100))

color, next_color = get_color(), get_color()
score, lines = 0, 0
record = '0'

sc.create_text(350, 10, text="TETRIS", font=(
    "WiGuru 2", 50), fill="Gold", anchor=NW)
sc.create_text(390, 580, text="score:", font=(
    "WiGuru 2", 40), fill="green", anchor=NW)
_score = sc.create_text(390, 660, text=str(
    score), font=("WiGuru 2", 20), fill="white", anchor=NW)
sc.create_text(390, 460, text="record:", font=(
    "WiGuru 2", 40), fill="Gold", anchor=NW)
_record = sc.create_text(390, 530, text=record, font=(
    "WiGuru 2", 20), fill="white", anchor=NW)

def speed(num):
    global V
    if num == 1:
        V = 2000
        game()
    elif num == 2:
        V = 600
        game()
    elif num == 3:
        V = 300
        game()

button_player = Button(sc, text='Просто', command=lambda: levell(1), font=(
    'WiGuru 2', 11), bd=8, bg='green', activebackground='white', foreground='white')
button_player.pack()
button_player.place(relx=0.68, rely=0.35, anchor=CENTER)

button_player1 = Button(sc, text='Средне', command=lambda: levell(
    2), font=('WiGuru 2', 11), bd=8, bg='yellow', activebackground='white')
button_player1.pack()
button_player1.place(relx=0.68, rely=0.45, anchor=CENTER)

button_player2 = Button(sc, text='Сложно', command=lambda: levell(3), font=(
    'WiGuru 2', 11), bd=8, bg='red', activebackground='white', foreground='white')
button_player2.pack()
button_player2.place(relx=0.68, rely=0.55, anchor=CENTER)

button_speed = Button(sc, text='скорость x1', command=lambda: speed(1), font=(
    'WiGuru 2', 11), bd=8, bg='green', activebackground='white', foreground='white')
button_speed.pack()
button_speed.place(relx=0.88, rely=0.35, anchor=CENTER)

button_speed1 = Button(sc, text='скорость x2', command=lambda: speed(
    2), font=('WiGuru 2', 11), bd=8, bg='yellow', activebackground='white')
button_speed1.pack()
button_speed1.place(relx=0.88, rely=0.45, anchor=CENTER)

button_speed2 = Button(sc, text='скорость x3', command=lambda: speed(3), font=(
    'WiGuru 2', 11), bd=8, bg='red', activebackground='white', foreground='white')
button_speed2.pack()
button_speed2.place(relx=0.88, rely=0.55, anchor=CENTER)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500, 5: 3500, 6: 9000}
anim_count, anim_speed, anim_limit = 0, 100, V

def move_obj(event):
    global rotate, anim_limit, dx, app_running
    if event.keysym == 'Up':
        rotate = True
    elif event.keysym == 'Down':
        anim_limit = 300
    elif event.keysym == 'Left':
        dx = -1
    elif event.keysym == 'Right':
        dx = 1
    elif event.keysym == 'space':
        if app_running:
            app_running = False
        else:
            app_running = True

game_sc.bind_all("<KeyPress-Up>", move_obj)
game_sc.bind_all("<KeyPress-Down>", move_obj)
game_sc.bind_all("<KeyPress-Left>", move_obj)
game_sc.bind_all("<KeyPress-Right>", move_obj)
game_sc.bind_all("<KeyPress-space>", move_obj)

def game():
    global figure, rotate, dx, number_level, app_running, record, next_figure, anim_count, anim_speed, anim_limit
    global score, lines, field, figures, scores, record, _score, _record, color, next_color, get_color
    dx, rotate = 0, False
    def check_borders():
        if figure[i][0] < 0 or figure[i][0] > W - 1:
            return False
        elif figure[i][1] > H - 1 or field[figure[i][1]][figure[i][0]]:
            return False
        return True
    while app_running:
        if app_running:
            record = get_record()
            # переместить х
            figure_old = deepcopy(figure)
            for i in range(number_level):
                figure[i][0] += dx
                if not check_borders():
                    figure = deepcopy(figure_old)
                    break
            # переместить y
            anim_count += anim_speed
            if anim_count > anim_limit:
                anim_count = 0
                figure_old = deepcopy(figure)
                for i in range(number_level):
                    figure[i][1] += 1
                    if not check_borders():
                        for i in range(number_level):
                            field[figure_old[i][1]][figure_old[i][0]] = color
                        figure, color = next_figure, next_color
                        next_figure, next_color = deepcopy(
                            choice(figures)), get_color()
                        anim_limit = V
                        break
            # вращать
            center = figure[0]
            figure_old = deepcopy(figure)
            if rotate:
                for i in range(number_level):
                    x = figure[i][1] - center[1]
                    y = figure[i][0] - center[0]
                    figure[i][0] = center[0] - x
                    figure[i][1] = center[1] + y
                    if not check_borders():
                        figure = deepcopy(figure_old)
                        break
            # контрольные линии
            line, lines = H - 1, 0
            for row in range(H-1, -1, -1):
                count = 0
                for i in range(W):
                    if field[row][i]:
                        count += 1
                    field[line][i] = field[row][i]
                if count < W:
                    line -= 1
                else:
                    lines += 1
            # вычислить счет
            score += scores[lines]
            # нарисовать фигуру
            for i in range(number_level):
                figure_rect_x = figure[i][0] * TILE
                figure_rect_y = figure[i][1] * TILE
                fig.append(game_sc.create_rectangle(figure_rect_x, figure_rect_y,
                                                    figure_rect_x+TILE, figure_rect_y+TILE, fill=rgb_to_hex(color)))
            # поле для рисования
            for y, raw in enumerate(field):
                for x, col in enumerate(raw):
                    if col:
                        figure_rect_x, figure_rect_y = x * TILE, y * TILE
                        fig.append(game_sc.create_rectangle(figure_rect_x, figure_rect_y,
                                                            figure_rect_x+TILE, figure_rect_y+TILE, fill=rgb_to_hex(col)))
            # нарисовать следующую_фигуру
            for i in range(number_level):
                figure_rect_x = next_figure[i][0] * TILE + 290
                figure_rect_y = next_figure[i][1] * TILE + 130
                fig2.append(sc.create_rectangle(figure_rect_x, figure_rect_y,
                            figure_rect_x+TILE, figure_rect_y+TILE, fill=rgb_to_hex(next_color)))
            # рисовать титулы
            sc.itemconfigure(_score, text=str(score))
            sc.itemconfigure(_record, text=record)
            # game over
            for i in range(W):
                if field[0][i]:
                    set_record(record, score)
                    field = [[0 for i in range(W)] for i in range(H)]
                    anim_count, anim_speed, anim_limit = 0, 100, V
                    score = 0
                    for item in grid:
                        game_sc.itemconfigure(
                            item, fill=rgb_to_hex(get_color()))
                        time.sleep(0.0001)
                        tk.update_idletasks()
                        tk.update()
                    for item in grid:
                        game_sc.itemconfigure(item, fill="")
            dx, rotate = 0, False
            tk.update_idletasks()
            tk.update()
            for id_fig in fig:
                game_sc.delete(id_fig)
            for id_fig in fig2:
                sc.delete(id_fig)
            fig.clear()
            fig2.clear()
        time.sleep(0.005)
tk.mainloop()