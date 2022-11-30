
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
delta = 20

def move_car():
    global car, delta
    if car.x > 1400:
        delta *= -1
    if car.x < 100:
        delta *= -1
    car.move(delta, 0)
    root.after(100, move_car)

root.after(100, move_car)
root.mainloop()

