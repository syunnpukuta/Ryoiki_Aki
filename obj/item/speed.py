from obj.item.item import Item
import tkinter as tk


class SpeedItem(Item):

    def __init__(self, canvas: tk.Canvas, x, y):
        super().__init__(canvas, x, y, "green")

    def effect(self, cannon: "Cannon"):
        cannon.delta += 0.3
