from _distutils_hack import override
import tkinter as tk

from obj.bullet import Bullet
from obj.machine import Machine


class Cannon(Machine):

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color, hp):
        super().__init__(canvas, x, y, width, height, color, 1)
        self.tag = "enemy"

    def repaint(self):
        self.y -= 1

