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
        car = Car(canvas, 20 + 70 * j, 20 + 50 * (i % 10), 60, 40, "red" if (i + j) % 2 == 0 else "blue")
        car.create_car()
        c.append(car)
    cars.append(c)


def console_input():
    print('10の位の値を行の番号，1の位の値を列の番号とし消したい車の番号を入力してください')
    num = input('>> ')
    # try:
    if 0 <= int(num) <= 99 :
        cars[int(num[0])][int(num[1])].delete()
        root.update()
    else:
        print("0~99の範囲を入力してください")
    # except:
    #     print("半角数字を入力してください")
    root.after(100, console_input)

root.after(100, console_input)

root.mainloop()

