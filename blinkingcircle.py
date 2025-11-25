import turtle
import time

def draw_circle(r, color):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)



turtle.speed(0)
turtle.hideturtle()

for i in range(10):
    turtle.clear()
    draw_circle(100, "black")   # Circle ON
    turtle.getscreen().update()
    time.sleep(0.5)

    turtle.clear()            # Circle OFF
    turtle.getscreen().update()
    time.sleep(0.5)

turtle.done()
