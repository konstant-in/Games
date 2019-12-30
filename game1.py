import tkinter as tk
from random import randint

WIDTH = 800
HEIGHT = 600
DELAY = 30


def mouse_click_handler(event):
    r = randint(20, 50)
    x = event.x
    y = event.y
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    create_ball(x, y, r, 'red', vx, vy)


def ins_handler(event):
    r = randint(20, 50)
    x = event.x
    y = event.y
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    create_ball(x, y, r, 'green', vx, vy)


def create_ball(x, y, r, color, vx, vy):
    ball = [canvas.create_oval(x, y, x + r, y + r, fill=color), vx, vy]
    balls.append(ball)
    return ball


def update(ball):
    canvas.move(ball[0], ball[1], ball[2])


def tick():
    for ball in balls:
        update(ball)
    root.after(DELAY, tick)


root = tk.Tk()
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind('<Button-1>', mouse_click_handler)
canvas.bind('<Button-3>', ins_handler)

balls = []

create_ball(10, 50, 20, 'blue', 5, 2)

tick()

root.mainloop()
