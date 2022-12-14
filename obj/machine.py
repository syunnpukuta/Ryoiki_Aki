from typing import TYPE_CHECKING
import tkinter as tk
from obj.obj import Obj
if TYPE_CHECKING:
    from obj.bullet import Bullet

class Machine(Obj):

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color, hp):
        super().__init__(canvas, x, y, width, height, color)
        self.hp = hp


    def on_bullet_hit(self, bullet: "Bullet"):
        if bullet.shoot_tag is not self.tag:
            self.hp -= bullet.damage
            bullet.on_hit(self)
            if self.hp <= 0:
                self.on_dead()

    def on_dead(self):
        self.delete()
        if "dead" in self.event_func:
            self.event_func["dead"]()