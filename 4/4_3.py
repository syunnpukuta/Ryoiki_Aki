import tkinter

from obj.cannon import Cannon
from obj.car import Car
from obj.obj import Obj

root = tkinter.Tk()
root.geometry("1600x900")

canvas = tkinter.Canvas(root, bg="white")
canvas.pack(fill=tkinter.BOTH, expand=True)

c = Cannon(canvas, 700, 700, 150, 100, "green")
c.create()

car = Car(canvas, 700, 100, 150, 100, "blue")
car.create()

def create_car():
    global car
    car = Car(canvas, 100, 100, 150, 100, "blue")
    car.set_event("dead", create_car)
    car.create()

car.set_event("dead", create_car)

def repaint():
    global car
    for i in Obj.objects:
        i.repaint()
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

    move_car()
    root.after(10, repaint)


def key_event(e):
    key = e.keysym
    if key == "space":
        c.shoot()
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