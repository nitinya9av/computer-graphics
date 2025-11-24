import turtle
import math

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def rotate_point(x, y, angle_deg):
    return (
        x * math.cos(math.radians(angle_deg)) - y * math.sin(math.radians(angle_deg)),
        x * math.sin(math.radians(angle_deg)) + y * math.cos(math.radians(angle_deg))
    )

# ---- USER INPUT ----
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

angle = float(input("Enter rotation angle in degrees: "))

turtle.tracer(0)
turtle.hideturtle()

draw_line(x1, y1, x2, y2, "black")

nx1, ny1 = rotate_point(x1, y1, angle)
nx2, ny2 = rotate_point(x2, y2, angle)

draw_line(nx1, ny1, nx2, ny2, "red")

turtle.update()
turtle.done()
