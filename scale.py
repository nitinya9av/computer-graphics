import turtle

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def scale_point(x, y, sx, sy):
    return x * sx, y * sy


# ---- USER INPUT ----
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

sx = float(input("Enter scaling factor Sx: "))
sy = float(input("Enter scaling factor Sy: "))

turtle.tracer(0)
turtle.hideturtle()

# Draw original line (Black)
draw_line(x1, y1, x2, y2, "black")

# Scale both endpoints
nx1, ny1 = scale_point(x1, y1, sx, sy)
nx2, ny2 = scale_point(x2, y2, sx, sy)

# Draw scaled line (Red)
draw_line(nx1, ny1, nx2, ny2, "red")

turtle.update()
turtle.done()
