import random
import time
import tkinter

from obj.cannon import Cannon
from obj.enemy.enemy1 import Enemy1
from obj.enemy.enemy2 import Enemy2
from obj.enemy.enemy3 import Enemy3
from obj.enemy.enemy4 import Enemy4
from obj.machine import Machine
from obj.obj import Obj

root = tkinter.Tk()
root.geometry("1600x900+100+100")

canvas = tkinter.Canvas(root, bg="white")
canvas.pack(fill=tkinter.BOTH, expand=True)

c = Cannon(canvas, 700, 700, 81, 54, "green", 10)
c.create()

hp = canvas.create_rectangle(0, 890, 1600, 900, fill="green", tags="hp")
text = canvas.create_text(100, 50, text="倒した数: 0", font=("", 20), tags="text")

cnt = 0
def repaint():
    t1 = time.time()
    global car, cnt
    for i in Obj.objects:
        i._repaint(cnt, c)
        if i.tag == "bullet" or i.tag == "item":
            continue
        ids = canvas.find_overlapping(i.x, i.y, i.x + i.width, i.y+i.height)
        ids = [j for j in ids if j not in i.parts + [1, 2, 3, 4]]
        try:
            hit_objs = set([Obj.parts2Obj[j] for j in ids])
            if len(hit_objs) > 0:
                for o in hit_objs:
                    if o.tag == "bullet":
                        i.on_bullet_hit(o)
                        break
                    else:
                        if o.tag == "enemy":
                            i.on_hit(o)

                    if i.tag == "cannon" and o.tag == "item":
                        o.on_hit(c)
        except:
            pass
        if c.is_dead:
            break
    if cnt % 197 == 0:
        Enemy1(canvas, random.randint(100, 1500), 0, 150, 100, "red", 3).create()
    if cnt % 367 == 0:
        Enemy2(canvas, random.randint(100, 1500), 0, 150, 100, "orange", 3).create()
    if cnt % 567 == 0:
        Enemy3(canvas, random.randint(100, 1500), 0, 150, 100, "yellow", 3).create()
    if cnt % 987 == 0:
        Enemy4(canvas, random.randint(100, 1500), 0, 150, 100, "black", 3).create()
    cnt += 1

    if not c.is_dead:
        root.after(10 - int((time.time() - time.time())), repaint)
    else:
        gameover()

def gameover():
    canvas.delete("all")
    canvas.create_text(800, 300, text="Game Over", font=("", 40), tags="text")
    canvas.create_text(800, 400, text="倒した数: "+str(Machine.defeat_cnt), font=("", 40), tags="text")


def key_press(e):
    key = e.keysym
    if key == "space":
        c.shoot()
    if key == "Up":
        c.u = True
    if key == "Down":
        c.d = True
    if key == "Left":
        c.l = True
    if key == "Right":
        c.r = True

root.bind("<KeyPress>", key_press)

def key_release(e):
    key = e.keysym
    if key == "Up":
        c.u = False
    if key == "Down":
        c.d = False
    if key == "Left":
        c.l = False
    if key == "Right":
        c.r = False

root.bind("<KeyRelease>", key_release)

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