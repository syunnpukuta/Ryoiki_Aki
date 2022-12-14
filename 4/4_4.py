import tkinter

from obj.cannon import Cannon
from obj.car import Car
from obj.obj import Obj

root = tkinter.Tk()
root.geometry("1600x900")

canvas = tkinter.Canvas(root, bg="white")
canvas.pack(fill=tkinter.BOTH, expand=True)

c = Cannon(canvas, 700, 700, 90, 60, "green", 1)
c.create()

car = Car(canvas, 700, 100, 150, 100, "blue", 1)
car.create()

def repaint():
    global car
    for i in Obj.objects:
        i._repaint_()
        ids = canvas.find_overlapping(i.x, i.y, i.x + i.width, i.y+i.height)
        ids = [j for j in ids if j not in i.parts + [1, 2]]
        hit_objs = set([Obj.parts2Obj[j] for j in ids])
        if len(hit_objs) > 0:
            for o in hit_objs:
                if o.tag == "bullet":
                    i.on_bullet_hit(o)
                    break
                else:
                    i.on_hit(o)

    root.after(10, repaint)


def key_event(e):
    key = e.keysym
    if key == "space":
        c.shoot()
    delta = 20
    x, y = 0, 0
    if key == "Up":
        if c.y >= delta:
            y -= delta
    if key == "Down":
        if c.y + c.height < 900-delta:
            y += delta
    if key == "Left":
        if c.x >= delta:
            x -= delta
    if key == "Right":
        if c.x + c.width < 1600 - delta:
            x += delta

    c.move(x, y)


root.bind("<KeyPress>", key_event)

delta = 10

def move_car():
    global car, delta
    if car.x > 1400:
        delta *= -1
    if car.x < 100:
        delta *= -1
    car.move(delta, 0)


root.after(10, repaint)
root.mainloop()