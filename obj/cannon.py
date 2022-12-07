from _distutils_hack import override
import tkinter as tk

from obj.bullet import Bullet
from obj.obj import Obj


class Cannon(Obj):

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color):
        super().__init__(canvas, x, y, width, height, color)
        self.tag = "cannon"


    def _create(self):
        self.parts.append(self.canvas.create_rectangle(
            self.x + self.width // 4,
            self.y,
            self.x + self.width - self.width // 4,
            self.y + self.height // 2,
            fill=self.color,
            tags=[self.id, self.tag]
        ))

        self.parts.append(self.canvas.create_rectangle(
            self.x,
            self.y + self.height // 2,
            self.x + self.width,
            self.y + self.height,
            fill=self.color,
            tags=[self.id, self.tag]
        ))

    def shoot(self):
        Bullet(self.canvas, self.x+self.width//2, self.y-10, 10, 10, "black", 0, -4).create()

