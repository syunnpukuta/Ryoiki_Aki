import json
import tkinter


root = tkinter.Tk()
root.geometry("1600x900")

# Canvasの作成
canvas = tkinter.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tkinter.BOTH, expand=True)

canvas.create_rectangle(300, 100, 700, 300, fill='black')
canvas.create_rectangle(100, 300, 900, 500, fill='black')
canvas.create_oval(200, 500, 400, 700, fill='black')
canvas.create_oval(600, 500, 800, 700, fill='black')
canvas.create_text(500, 770, text="Shuntaro Kitagawa", font=("HG丸ｺﾞｼｯｸM-PRO",30))
root.mainloop()