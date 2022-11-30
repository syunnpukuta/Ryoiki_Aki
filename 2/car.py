import tkinter as tk

class Car:

    def __init__(self, canvas: tk.Canvas, x, y, width, height, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.top = None
        self.bottom = None
        self.tire1 = None
        self.tire2 = None

    def create_car(self):
        tire = self.height // 5
        self.top = self.canvas.create_rectangle(self.x+self.width//4, self.y, self.x+self.width-self.width//4, self.y+self.height//5*2, fill=self.color)
        self.bottom = self.canvas.create_rectangle(self.x, self.y+self.height//5*2, self.x+self.width, self.y+self.height//5*4, fill=self.color)
        self.tire1 = self.canvas.create_oval(self.x+self.width//4-tire//2, self.y+self.height//5*4, self.x+self.width//4+tire//2, self.y+self.height, fill='black')
        self.tire2 = self.canvas.create_oval(self.x+self.width-self.width//4-tire//2, self.y+self.height//5*4, self.x+self.width-self.width//4+tire//2, self.y+self.height, fill='black')
        return [self.top, self.bottom, self.tire1, self.tire2]

    def delete(self):
        self.canvas.delete(self.top)
        self.canvas.delete(self.bottom)
        self.canvas.delete(self.tire1)
        self.canvas.delete(self.tire2)