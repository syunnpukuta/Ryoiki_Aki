from _distutils_hack import override
import tkinter as tk

from obj.machine import Machine
from obj.obj import Obj



class Bullet(Obj):
    def __init__(self, canvas: tk.Canvas, x, y, width, height, color, dx, dy, shoot_tag, damage):
        super().__init__(canvas, x, y, width, height, color)
        self.tag = "bullet"
        self.dx = dx
        self.dy = dy
        self.damage = damage
        self.shoot_tag = shoot_tag

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

    def repaint(self, cnt, cannon:"Cannon"):
        self.move(self.dx, self.dy)

    def on_hit(self, obj: Machine):
        self.delete()