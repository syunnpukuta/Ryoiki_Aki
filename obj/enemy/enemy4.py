import random

from obj.bullet.bullet2 import Bullet2
from obj.enemy.enemy import Enemy
from obj.item.speed import SpeedItem
from obj.item.health import HealthItem
from obj.item.interval import IntervalItem


class Enemy4(Enemy):

    item = [
        HealthItem,
        HealthItem,
        SpeedItem,
        IntervalItem,
    ]

    def on_dead(self):
        super().on_dead()
        random.choice(Enemy4.item)(self.canvas, self.x, self.y).create()

    def repaint(self, cnt, cannon:"Cannon"):
        self.move(0, 1)
        if cnt % 200 == 0:
            Bullet2(self.canvas, self.x, self.y, 10, 10, "red", 0, 0, self.tag, 1).create()
