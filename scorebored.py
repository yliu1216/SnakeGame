from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 24, "normal")

class Scorebored(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("my_file.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 190)
       # self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        #self.clear()
        self.update_scoreboard()

    #def game_over(self):
      #  self.goto(0, 0)
       # self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def highest_score(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("my_file.txt", mode="w") as file:
                file.write(f"{int(self.high_score)}")
        self.score=0
        self.update_scoreboard()