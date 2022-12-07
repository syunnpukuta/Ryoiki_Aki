from _distutils_hack import override
import tkinter as tk

from obj.obj import Obj


class Bullet(Obj):
    def __init__(self, canvas: tk.Canvas, x, y, width, height, color, dx, dy, root=None):
        super().__init__(canvas, x, y, width, height, color)
        self.tag = "bullet"
        self.dx = dx
        self.dy = dy

    def _create(self):
        self.parts.append(
            self.canvas.create_oval(
                self.x,
                self.y,
                self.x + self.width,
                self.y + self.height,
                fill=self.color,
                tags=[self.id, self.tag]
            )
        )

    def repaint(self):
        self.move(self.dx, self.dy)

