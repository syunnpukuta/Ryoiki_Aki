import tkinter as tk

from obj.bullet.bullet import Bullet


class Beam(Bullet):
    def __init__(self, canvas: tk.Canvas, x, y, width, height, color, dx, dy, shoot_tag, damage, cnt):
        super().__init__(canvas, x, y, width, height, color,  dx, dy, shoot_tag, damage)
        self.cnt = cnt
        self.m1 = False
        self.m2 = False

    def _create(self):
            self.parts.append(
                self.canvas.create_rectangle(
                    self.x+100000,
                    self.y,
                    10,
                    10000,
                    fill="yellow",
                    tags=[self.id, self.tag]
                )
            )
            self.parts.append(
                self.canvas.create_rectangle(
                    self.x+100000,
                    self.y,
                    self.x+100000+10,
                    self.y+100,
                    fill="red",
                    tags=[self.id, self.tag]
                )
            )

    def repaint(self, cnt, cannon:"Cannon"):
        print(cnt, self.cnt, cnt-self.cnt)
        if cnt - self.cnt == 300 and not self.m2:
            self.move(-100000, 0)
            self.m2 = True
        if cnt - self.cnt == 100 and not self.m1:
            self.move(-100000, 0)
            self.m1 = True

    # def on_hit(self, obj: Machine):
    #     pass