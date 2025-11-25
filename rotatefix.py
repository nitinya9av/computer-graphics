import turtle
import math

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

# Rotate (x, y) around pivot (h, k)
def rotate_point_pivot(x, y, h, k, angle_deg):
    angle = math.radians(angle_deg)

    # Step 1: translate to origin
    x -= h
    y -= k

    # Step 2: rotate
    xr = x * math.cos(angle) - y * math.sin(angle)
    yr = x * math.sin(angle) + y * math.cos(angle)

    # Step 3: translate back
    return xr + h, yr + k


# ---- USER INPUT ----
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

h = int(input("Enter pivot x (h): "))
k = int(input("Enter pivot y (k): "))

angle = float(input("Enter rotation angle in degrees: "))

turtle.tracer(0)
turtle.hideturtle()

# Draw original line (black)
draw_line(x1, y1, x2, y2, "black")

# Rotate both points about pivot
nx1, ny1 = rotate_point_pivot(x1, y1, h, k, angle)
nx2, ny2 = rotate_point_pivot(x2, y2, h, k, angle)

# Draw rotated line (red)
draw_line(nx1, ny1, nx2, ny2, "red")

# Draw pivot point (blue dot)
turtle.penup()
turtle.goto(h, k)
turtle.dot(10, "blue")

turtle.update()
turtle.done()
