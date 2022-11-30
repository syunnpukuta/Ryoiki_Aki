
import tkinter

from car import Car

root = tkinter.Tk()
root.geometry("1600x900")

# Canvasの作成
canvas = tkinter.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tkinter.BOTH, expand=True)

car = Car(canvas, 200, 200, 150, 100, "blue")
car.create_car()

def key_event(e):
    global car, root
    delta = 20
    key = e.keysym
    x, y = 0, 0
    if key == "Up":
        if car.y >= delta:
            y -= delta
    if key == "Down":
        if car.y + car.height < 900-delta:
            y += delta
    if key == "Left":
        if car.x >= delta:
            x -= delta
    if key == "Right":
        if car.x + car.width < 1600 - delta:
            x += delta

    car.move(x, y)


root.bind("<KeyPress>", key_event)

root.mainloop()

