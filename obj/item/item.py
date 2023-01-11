from obj.obj import Obj
import tkinter as tk

class Item(Obj):

    def __init__(self, canvas: tk.Canvas, x, y, color):
        super().__init__(canvas, x, y, 20, 20, color)
        self.tag = "item"

    def _create(self):
        self.parts.append(self.canvas.create_rectangle(
            self.x - self.width/2,
            self.y - self.height // 2,
            self.x + self.width // 2,
            self.y + self.height // 2,
            fill=self.color,
            tags=[self.id, self.tag]
        ))

    def repaint(self, cnt, cannon:"Cannon"):
        self.move(0, 3)

    def effect(self, cannon: "Cannon"):
        pass

    def on_hit(self, cannon: "Cannon"):
        self.effect(cannon)
        self.delete()
