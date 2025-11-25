import turtle
import time

def draw_circle(r, color):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)

# ------------ PARAMETERS --------------
r = 100
blinks = 10
delay = 0.5

turtle.speed(0)
turtle.hideturtle()

for i in range(blinks):
    turtle.clear()
    draw_circle(r, "black")   # Circle ON
    turtle.getscreen().update()
    time.sleep(delay)

    turtle.clear()            # Circle OFF
    turtle.getscreen().update()
    time.sleep(delay)

turtle.done()
