
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

c = Cannon(canvas, 700, 700, 150, 100, "green", 1)
c.create()

cnt = 0
def repaint():
    global cnt
    for i in Obj.objects:
        i.repaint()
    if cnt % 10 == 0:
        c.shoot()
    cnt+=1
    root.after(10, repaint)

root.after(10, repaint)
root.mainloop()

