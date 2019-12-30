import tkinter as tk
from random import randint

# Константы
WIDTH = 800
HEIGHT = 600
DELAY = 50
TIMER = 3000


def pulja(event):
    '''создание пулек'''
    r = 10
    x = event.x
    y = event.y
    vx = 20
    vy = 0
    color = 'red'
    Ball.create(x, y, vx, vy, r, color, 'g1')


def mishen():
    '''создание целей'''
    r = randint(20, 100)
    x = randint(WIDTH / 2, WIDTH)
    y = HEIGHT
    vx = 0
    vy = randint(-3, -1)
    color = 'blue'
    Ball.create(x, y, vx, vy, r, color, 'g2')
    # black
    # white
    root.after(TIMER, mishen)


def popal(event):
    x = event.x
    y = event.y
    print(event.x, event.y)
    print('Попал')


class Ball:
    def __init__(self, x, y, vx, vy, r, color, tag):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.color = color
        self.tag = tag
        self.ball_id = battlefield.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, fill=self.color,
                                               tag=self.tag)

    @classmethod
    def create(cls, x, y, vx, vy, r, color, grup):
        objects.append(cls(x, y, vx, vy, r, color, grup))

    def update(self):
        battlefield.move(self.ball_id, self.vx, self.vy)


def update_world():
    for obj in objects:
        obj.update()
        battlefield.tag_bind('g2', '<Button-1>', popal)
        # "число объектов: len(objects)
    root.after(DELAY, update_world)


# создаем главное окно и поле боя
objects = []
root = tk.Tk()
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
battlefield = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='green')
battlefield.pack()
battlefield.bind('<Button-3>', pulja)
mishen()
update_world()
root.mainloop()
