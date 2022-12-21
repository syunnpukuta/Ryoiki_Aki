import math

from obj.bullet.bullet import Bullet
from obj.enemy.enemy import Enemy


class Enemy1(Enemy):

    def repaint(self, cnt, cannon:"Cannon"):
        self.move(0, 2)

        if self.y == 800:
            self.delete()
            for i in range(8):
                Bullet(self.canvas, self.x, self.y, 10, 10, "red", 4*math.sin(math.pi/4*i), 4*math.cos(math.pi/4*i), self.tag, 1).create()


