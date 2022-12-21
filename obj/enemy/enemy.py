from obj.machine import Machine
import tkinter as tk

class Enemy(Machine):

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color, hp):
        super().__init__(canvas, x, y, width, height, color, hp)
        self.tag = "enemy"

    def on_bullet_hit(self, bullet: "Bullet"):
        super(Enemy, self).on_bullet_hit(bullet)
        if self.is_dead:
            Machine.defeat_cnt += 1
            self.canvas.delete("text")
            text = self.canvas.create_text(100, 50, text="倒した数: " + str(Machine.defeat_cnt), font=("", 20),
                                               tags="text")

    def _create(self):
        self.parts.append(self.canvas.create_rectangle(
            self.x + self.width // 4,
            self.y +self.height// 2,
            self.x + self.width - self.width // 4,
            self.y + self.height,
            fill=self.color,
            tags=[self.id, self.tag]
        ))

        self.parts.append(self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height//2,
            fill=self.color,
            tags=[self.id, self.tag]
        ))