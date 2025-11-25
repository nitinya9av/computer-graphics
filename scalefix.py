import turtle

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def scale_about_fixed_point(x, y, sx, sy, xf, yf):
    # Translate point relative to fixed point → Scale → Translate back
    new_x = xf + (x - xf) * sx
    new_y = yf + (y - yf) * sy
    return new_x, new_y

# ---- USER INPUT ----
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

sx = float(input("Enter scaling factor Sx: "))
sy = float(input("Enter scaling factor Sy: "))

xf = int(input("Enter fixed point Xf: "))
yf = int(input("Enter fixed point Yf: "))

turtle.tracer(0)
turtle.hideturtle()

# Draw original line (Black)
draw_line(x1, y1, x2, y2, "black")

# Apply scaling about fixed point
nx1, ny1 = scale_about_fixed_point(x1, y1, sx, sy, xf, yf)
nx2, ny2 = scale_about_fixed_point(x2, y2, sx, sy, xf, yf)

# Draw scaled line (Red)
draw_line(nx1, ny1, nx2, ny2, "red")

turtle.update()
turtle.done()
