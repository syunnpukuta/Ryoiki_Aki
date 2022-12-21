from __future__ import annotations
import tkinter as tk
import uuid




from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cannon import Cannon
#     from bullet import Bullet


class Obj:

    objects = []
    parts2Obj = {}

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.parts = []
        self.event_func = {}

        self.id = str(uuid.uuid4())
        self.tag = ""
        self.is_dead = False
        Obj.objects.append(self)

    def create(self):
        self._create()
        for i in self.parts:
            Obj.parts2Obj[i] = self

    def _create(self):
        pass

    def check_area(self) -> bool:
        if not -1000< self.x < 2000:
            self.delete()
            return False
        elif not -1000< self.y < 2000:
            self.delete()
            return False

        return True

    def _repaint(self, cnt, cannon: "Cannon"):
        if self.check_area():
            self.repaint(cnt, cannon)

    def repaint(self, cnt, cannon:"Cannon"):
        pass

    def delete(self):
        self.is_dead = True
        self.canvas.delete(self.id)
        try:
            Obj.objects.remove(self)
        except ValueError:
            pass

    def move(self, x, y):
        self.x += x
        self.y += y
        self.canvas.move(self.id, x, y)

    def set_event(self, event, func):
        self.event_func[event] = func
