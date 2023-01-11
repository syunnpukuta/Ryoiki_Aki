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
        self.interval = 20
        self.delta = 8



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
        if self.u:
            if self.y >= self.delta:
                self.move(0,-self.delta)
        if self.d:
            if self.y + self.height < 900 - self.delta:
                self.move(0, self.delta)
        if self.l:
            if self.x >= self.delta:
                self.move(-self.delta, 0)

        if self.r:
            if self.x + self.width < 1600 - self.delta:
                self.move(self.delta, 0)
        if cnt % self.interval == 0:
            self.shoot()


    def shoot(self):
        Bullet(self.canvas, self.x+self.width//2, self.y-10, 10, 10, "black", 0, -4, self.tag, 1).create()

    def on_bullet_hit(self, bullet: "Bullet"):
        hp = self.hp
        if bullet.shoot_tag != "cannon":
            super(Cannon, self).on_bullet_hit(bullet)
            d = hp - self.hp
            self.canvas.move("hp", -(1600/self.max_hp) * d, 0)
            h = self.hp / self.max_hp

    def add_hp(self, i):
        self.hp += i
        self.canvas.move("hp", (1600 / self.max_hp))

    def on_hit(self, obj: "Obj"):
        if obj.tag == "enemy":
            obj.hp -= 10
            self.delete()
            if obj.hp <= 0:
                obj.on_dead()