import turtle
import time

def draw_circle(r, color):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)

# ------------ USER INPUT --------------
r = int(input("Enter radius of circle: "))
blinks = int(input("Enter number of blinks: "))
delay = float(input("Enter delay (seconds): "))

turtle.tracer(0)
turtle.hideturtle()

for i in range(blinks):
    draw_circle(r, "black")   # Circle ON
    turtle.update()
    time.sleep(delay)

    turtle.clear()            # Circle OFF
    turtle.update()
    time.sleep(delay)

turtle.done()
