from car import Car
import tkinter


root = tkinter.Tk()
root.geometry("1600x900")

# Canvasの作成
canvas = tkinter.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tkinter.BOTH, expand=True)

cars = []

for i in range(10):
    c = []
    for j in range(10):
        car = Car(canvas, 20+70*j, 20+50*(i%10), 60, 40, "red" if (j + i) % 2 == 0 else "blue")
        car.create_car()
        c.append()
    cars.append(c)
root.mainloop()