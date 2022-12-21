from obj.bullet.bullet import Bullet
from obj.enemy.enemy import Enemy


class Enemy3(Enemy):



    def repaint(self, cnt, cannon:"Cannon"):
        self.move(0, 1)

        if cnt % 150 == 0:
            Bullet(self.canvas, self.x + self.width // 2, self.y + 15, 15, 15, "yellow", -5, 4, self.tag, 1).create()
            Bullet(self.canvas, self.x + self.width // 2, self.y + 15, 15, 15, "yellow", 0, 4, self.tag, 1).create()
            Bullet(self.canvas, self.x + self.width // 2, self.y + 15, 15, 15, "yellow", 5, 4, self.tag, 1).create()



