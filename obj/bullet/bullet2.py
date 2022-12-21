import math

from obj.bullet.bullet import Bullet
from obj.cannon import Cannon


class Bullet2(Bullet):

    def repaint(self, cnt, cannon: "Cannon"):
        s = 5
        vx = cannon.x - self.x
        vy = cannon.y - self.y
        l = math.sqrt(vx**2 + vy**2)
        vx2 = vx / l
        vy2 = vy / l
        vx3 = vx2 * s
        vy3 = vy2 * s
        self.move(min(vx3, 3), 5)
