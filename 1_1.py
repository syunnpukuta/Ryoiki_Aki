import json
import tkinter


root = tkinter.Tk()
root.geometry("1600x900")

# Canvasの作成
canvas = tkinter.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tkinter.BOTH, expand=True)

canvas.create_rectangle(100, 100, 900, 400, fill='black')

# root.after(100, move)

root.mainloop()