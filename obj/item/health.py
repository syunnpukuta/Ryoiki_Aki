from obj.item.item import Item
import tkinter as tk


class HealthItem(Item):

    def __init__(self, canvas: tk.Canvas, x, y):
        super().__init__(canvas, x, y, "pink")

    def effect(self, cannon: "Cannon"):
        cannon.add_hp(1)
