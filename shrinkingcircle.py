import turtle
import time

def draw_circle(r, color):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.circle(r)

# --------- Fixed Values ----------
radius = 120      # starting radius
steps = 40        # number of shrinking steps
delay = 0.05      # delay between frames

turtle.tracer(0)
turtle.hideturtle()

dr = radius / steps   # radius change per step

# ---- SHRINK ----
for i in range(steps + 1):
    turtle.clear()
    draw_circle(radius - i * dr, "black")
    turtle.update()
    time.sleep(delay)

# ---- GROW BACK ----
for i in range(steps + 1):
    turtle.clear()
    draw_circle(i * dr, "black")
    turtle.update()
    time.sleep(delay)

turtle.done()
