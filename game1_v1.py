import tkinter as tk
from random import randint

# Константы
WIDTH = 800
HEIGHT = 600
DELAY = 30


def left_click(event):
    # создание пулек
    r = 20
    x = event.x
    y = event.y
    vx = 20
    vy = 0
    create_ball(x, y, r, 'red', vx, vy)


def right_click(event):
    # создание целей
    r = randint(20, 100)
    x = event.x
    y = event.y
    vx = randint(-2, 2)
    vy = randint(-2, 2)
    create_ball(x, y, r, 'blue', vx, vy)


def create_ball(x, y, r, color, vx, vy):
    ball_id = [battlefield.create_oval(x, y, x + r, y + r, fill=color), vx, vy]
    objects.append(ball_id)
    return ball_id


class Ball:
    def __init__(self, x, y, r, color, vx, vy):
        # self.ball_id =
        self.y = y
        self.x = x
        self.vy = vy
        self.vx = vx
        self.r = r
        self.color = color

    @classmethod
    def create(cls, x, y, r, color, vx, vy):
        return cls.__init__(x, y, r, color, vx, vy)


def update(ball):
    battlefield.move(ball[0], ball[1], ball[2])


def update_world():
    for obj in objects:
        update(obj)
    root.after(DELAY, update_world)


# создаем главное окно и поле боя
root = tk.Tk()
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
battlefield = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='green')
battlefield.pack()
battlefield.bind('<Button-1>', left_click)
battlefield.bind('<Button-3>', right_click)
objects = []
update_world()
root.mainloop()
