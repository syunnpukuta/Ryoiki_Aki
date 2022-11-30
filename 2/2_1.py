from car import Car
import tkinter


root = tkinter.Tk()
root.geometry("1600x900")

# Canvasの作成
canvas = tkinter.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tkinter.BOTH, expand=True)

Car(canvas, 50, 50, 150, 100, "red").create_car()
Car(canvas, 150, 150, 300, 200, "blue").create_car()

root.mainloop()