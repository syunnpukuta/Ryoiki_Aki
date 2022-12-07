import tkinter as tk
import uuid

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
        Obj.objects.append(self)

    def create(self):
        self._create()
        for i in self.parts:
            Obj.parts2Obj[i] = self

    def _create(self):
        pass

    def repaint(self):
        pass

    def delete(self):
        self.canvas.delete(self.id)
        try:
            Obj.objects.remove(self)
        except ValueError:
            pass

        if "dead" in self.event_func:
            self.event_func["dead"]()

    def move(self, x, y):
        self.x += x
        self.y += y
        self.canvas.move(self.id, x, y)

    def on_hit(self, obj):
        pass

    def on_bullet_hit(self, bullet):
        pass

    def on_dead(self):
        if "dead" in self.event_func:
            self.event_func["dead"]()

    def set_event(self, event, func):
        self.event_func[event] = func
