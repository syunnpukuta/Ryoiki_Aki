from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from obj.obj import Obj
if TYPE_CHECKING:
    from obj.bullet.bullet import Bullet

class Machine(Obj):
    defeat_cnt = 0

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color, hp):
        super().__init__(canvas, x, y, width, height, color)
        self.hp = hp


    def on_bullet_hit(self, bullet: "Bullet"):
        if bullet.shoot_tag is not self.tag:
            self.hp -= bullet.damage
            bullet.on_hit(self)
            if self.hp <= 0:
                # if self.tag == "enemy":
                #     Machine.defeat_cnt += 1
                #     self.canvas.delete("text")
                #     text = self.canvas.create_text(100, 50, text="倒した数: "+str(Machine.defeat_cnt), font=("", 20), tags="text")
                self.on_dead()

    def on_dead(self):
        self.delete()
        if "dead" in self.event_func:
            self.event_func["dead"]()

    def on_hit(self, obj: __class__):
        pass
        # if obj.tag == "enemy":
        #     obj.hp -= 10
        #     self.delete()
        #     if obj.hp <= 0:
        #         obj.on_dead()