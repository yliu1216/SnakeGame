# snake game
# 1. create a snake body
# 2. Move the snake
# 3. Control the snake
# 4. Detect collision with wall
# 5. Detect collision with tail
import turtle
import pandas



from turtle import Turtle, Screen
from snake import Snake
from score import food
from scorebored import Scorebored
import time
screen=Screen()
screen.setup(1000, 450)
screen.bgcolor("black")
screen.title("Yingwei's Snake Game")
screen.tracer(0)


#file=open("my_file.txt")
#contents=file()
#print(contents)
#file.close()

#with open("my_file.txt", mode="a") as file:
 #   file.write("\nHello.")





#starting_position=[(0, 0), (-20, 0), (-40, 0)]
#segements=[]
n_turtle=Turtle()



# 1. snake body
"""
for position in starting_position:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(position)
    segements.append(new_turtle)
"""
snake = Snake()
snake.create_snake()
screen.update()

food = food()
scorebored=Scorebored()


screen.listen()
screen.onkey(snake.move_forwards, "Up")
screen.onkey(snake.move_backwards, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")



game_is_on=True
# 2. Move the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_extend()
        scorebored.increase_score()


    # detect collision with wall
    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 205 or snake.head.ycor() < -205:
        #game_is_on = False
        #corebored.game_over()
        scorebored.highest_score()
        snake.reset()

    #detect collision with tail
    for segement in snake.segments[1:]:
        if segement==snake.head:
            pass
        elif snake.head.distance(segement) < 10:
            scorebored.highest_score()
            snake.reset()


         #game_is_on=False
          # scorebored.game_over()
           # scorebored.highest_score()

        """
        if segement == snake.head:
            pass
        elif snake.head.distance(segement)<10:
            game_is_on=False
            scorebored.Gameover()
        """


"""    
    for seg_num in range(len(segements)-1, 0, -1):
        new_x = segements[seg_num-1].xcor()
        new_y = segements[seg_num-1].ycor()
        segements[seg_num].goto(new_x, new_y)
    segements[0].forward(20)

"""






"""
new_turtle2 = Turtle(shape="square")
new_turtle2.color("white")
new_turtle2.goto(-20, 0)

new_turtle3 = Turtle(shape="square")
new_turtle3.color("white")
new_turtle3.goto(-40, 0)
"""



screen.exitonclick()