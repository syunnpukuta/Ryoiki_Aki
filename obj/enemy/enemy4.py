from obj.bullet.bullet2 import Bullet2
from obj.enemy.enemy import Enemy


class Enemy4(Enemy):

    def repaint(self, cnt, cannon:"Cannon"):
        self.move(0, 0)
        if cnt % 200 == 0:
            Bullet2(self.canvas, self.x, self.y, 10, 10, "red", 0, 0, self.tag, 1).create()
