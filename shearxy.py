import turtle

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def shear_xy(x, y, kx, ky):
    nx = x + kx * y       # X-direction shear
    ny = y + ky * x       # Y-direction shear
    return nx, ny


# ---- USER INPUT ----
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
kx = float(input("Enter shear factor in X direction: "))
ky = float(input("Enter shear factor in Y direction: "))

turtle.tracer(0)
turtle.hideturtle()

# Draw original line
draw_line(x1, y1, x2, y2, "black")

# Apply combined shear
nx1, ny1 = shear_xy(x1, y1, kx, ky)
nx2, ny2 = shear_xy(x2, y2, kx, ky)

# Draw sheared line
draw_line(nx1, ny1, nx2, ny2, "red")

turtle.update()
turtle.done()
