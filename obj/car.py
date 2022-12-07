import random
import tkinter as tk
import uuid

from obj.obj import Obj


class Car(Obj):

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color):
        super().__init__(canvas, x, y, width, height, color)
        self.tag = "car"

    def _create(self):
        tire = self.height // 5
        self.parts.extend([self.canvas.create_rectangle(
            self.x + self.width // 4,
            self.y,
            self.x + self.width - self.width // 4,
            self.y + self.height // 5 * 2,
            fill=self.color,
            tags=[self.id, "car"]
        ),
        self.canvas.create_rectangle(
            self.x,
            self.y + self.height // 5 * 2,
            self.x + self.width,
            self.y + self.height // 5 * 4,
            fill=self.color,
            tags=[self.id, "car"]
        ),
        self.canvas.create_oval(
            self.x + self.width // 4 - tire // 2,
            self.y + self.height // 5 * 4,
            self.x + self.width // 4 + tire // 2,
            self.y + self.height,
            fill='black',
            tags=[self.id, "car"]
        ),
        self.canvas.create_oval(
            self.x + self.width - self.width // 4 - tire // 2,
            self.y + self.height // 5 * 4,
            self.x + self.width - self.width // 4 + tire // 2,
            self.y + self.height,
            fill='black',
            tags=[self.id, "car"]
        ),])

    def on_bullet_hit(self, bullet):
        self.delete()