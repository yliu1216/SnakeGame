import random
import turtle
from turtle import Turtle
import random
SCORE=0
COLOR=["blue", "green", "red", "yellow"]
turtle.colormode(255)

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.random_color()
        self.shape("circle")
        self.color(random.choice(COLOR))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()



    def refresh(self):
        random_x = random.randint(-480, 480)
        random_y = random.randint(-205, 205)
        self.goto(random_x, random_y)


    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors = (r, g, b)
        return colors
"""elf.color
    def score(self):
        new_turtle=Turtle()

        new_turtle.write(self, False, "center", 12)
"""