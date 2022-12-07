
import tkinter

from car import Car
from obj.cannon import Cannon
from obj.obj import Obj

root = tkinter.Tk()
root.geometry("1600x900")

# Canvasの作成
canvas = tkinter.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tkinter.BOTH, expand=True)

c = Cannon(canvas, 700, 700, 150, 100, "green")
c.create()

def repaint():
    global cnt

    for i in Obj.objects:
        i.repaint()
    root.after(10, repaint)


def key_event(e):
    key = e.keysym
    if key == "space":
        c.shoot()
root.bind("<KeyPress>", key_event)


root.after(10, repaint)
root.mainloop()

