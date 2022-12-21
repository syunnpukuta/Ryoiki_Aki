import tkinter as tk

from obj.bullet.bullet import Bullet
from obj.machine import Machine


class Cannon(Machine):

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color, hp):
        super().__init__(canvas, x, y, width, height, color, hp)
        self.tag = "cannon"
        self.u = False
        self.d = False
        self.r = False
        self.l = False
        self.max_hp = hp


    def _create(self):
        self.parts.append(self.canvas.create_rectangle(
            self.x + self.width // 4,
            self.y,
            self.x + self.width - self.width // 4,
            self.y + self.height // 2,
            fill=self.color,
            tags=[self.id, self.tag]
        ))

        self.parts.append(self.canvas.create_rectangle(
            self.x,
            self.y + self.height // 2,
            self.x + self.width,
            self.y + self.height,
            fill=self.color,
            tags=[self.id, self.tag]
        ))

    def repaint(self, cnt, cannon:"Cannon"):
        delta = 8
        if self.u:
            if self.y >= delta:
                self.move(0,-delta)
        if self.d:
            if self.y + self.height < 900 - delta:
                self.move(0, delta)
        if self.l:
            if self.x >= delta:
                self.move(-delta, 0)

        if self.r:
            if self.x + self.width < 1600 - delta:
                self.move(delta, 0)

    def shoot(self):
        Bullet(self.canvas, self.x+self.width//2, self.y-10, 10, 10, "black", 0, -4, self.tag, 1).create()

    def on_bullet_hit(self, bullet: "Bullet"):
        super(Cannon, self).on_bullet_hit(bullet)
        if bullet.shoot_tag != "cannon":
            self.canvas.move("hp", 0, 0)
            self.canvas.move("hp", -(1600-(1600*(self.hp/self.max_hp))), 0)
            h = self.hp / self.max_hp
            if h > 0.5:
                self.canvas.itemconfig("hp", fill="green")
            elif h > 0.3:
                self.canvas.itemconfig("hp", fill="yellow")
            else:
                self.canvas.itemconfig("hp", fill="red")
            print(self.hp)
