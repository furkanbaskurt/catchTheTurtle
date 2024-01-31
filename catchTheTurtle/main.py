import turtle
import random
import time
from tkinter import *


drawingBoard = turtle.Screen()
drawingBoard.title("Catch The Turtle")
drawingBoard.bgcolor("light blue")

turtleInstance = turtle.Turtle()
turtleInstance.color("green")
turtleInstance.shape(name="turtle")
turtleInstance.penup()
turtleInstance.hideturtle()
turtleInstance.turtlesize(stretch_len=2, stretch_wid=2)

point = 0

scoreText = Label(text=f"SCORE: {point}")
scoreText.pack(side=LEFT)

timeText = Label(text="Time Left: 10")
timeText.pack(side=RIGHT)


def score(x, y):
    global point
    point += 1
    scoreText.config(text=f"SCORE: {point}")


turtleInstance.onclick(fun=score)


def start():
    global point
    scoreText.config(text=f"SCORE: {point}")
    seconds = 10
    turtleInstance.showturtle()

    while seconds > 0:
        time.sleep(1)
        seconds -= 1
        timeText.config(text=f"Time Left: {seconds}")
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        turtleInstance.goto(x, y)

    timeText.config(text="Time's up! GAME OVER!")
    point = 0
    turtleInstance.hideturtle()


button = Button(drawingBoard.getcanvas().master, text="START", command=start, bd=10)
button.pack(side=BOTTOM)
button.config(height=2, width=10)

if point == 0:
    button.config(command=start)

turtle.mainloop()
