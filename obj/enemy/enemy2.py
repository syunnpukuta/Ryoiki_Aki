import math
from obj.enemy.enemy import Enemy


class Enemy2(Enemy):

    def repaint(self, cnt, cannon:"Cannon"):
        self.move(4*math.cos(math.pi/4*(cnt//20)), 4)



