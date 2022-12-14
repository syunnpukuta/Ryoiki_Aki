from _distutils_hack import override
import tkinter as tk

from obj.bullet import Bullet
from obj.machine import Machine


class Cannon(Machine):

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color, hp):
        super().__init__(canvas, x, y, width, height, color, 1)
        self.tag = "cannon"
        self.t = False
        self.b = False
        self.r = False
        self.l = False


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

    def repaint(self):
        delta = 20
        if self.t:
            if self.y >= delta:
                self.y -= delta
        if self.b:
            if self.y + self.height < 900 - delta:
                self.y += delta
        if self.l:
            if self.x >= delta:
                self.x -= delta
        if self.r:
            if self.x + self.width < 1600 - delta:
                self.x += delta

    def shoot(self):
        Bullet(self.canvas, self.x+self.width//2, self.y-10, 10, 10, "black", 0, -4, self.tag, 1).create()

