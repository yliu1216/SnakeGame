from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
n_turtle=Turtle()
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segements(position)

    def add_segements(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def snake_extend(self):
        self.add_segements(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_forwards(self):
        self.segments[0].setheading(90)

    def move_backwards(self):
        self.segments[0].setheading(270)
        self.segments[0].forward(10)

    def turn_left(self):
        self.segments[0].setheading(180)
        self.segments[0].forward(10)

    def turn_right(self):
        self.segments[0].setheading(0)
        self.segments[0].forward(10)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
