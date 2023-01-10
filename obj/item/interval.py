from obj.item.item import Item
import tkinter as tk


class IntervalItem(Item):

    def __init__(self, canvas: tk.Canvas, x, y):
        super().__init__(canvas, x, y, "red")

    def effect(self, cannon: "Cannon"):
        cannon.interval -= 1

        cannon.interval = max(1, cannon.interval)
