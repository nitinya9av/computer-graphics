import turtle

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def shear_x(x, y, k):
    return x + k * y, y   # Shearing in X-axis


# ---- USER INPUT ----
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
k  = float(input("Enter shear factor k: "))

turtle.tracer(0)
turtle.hideturtle()

# Draw original line
draw_line(x1, y1, x2, y2, "black")

# Apply X-shear
nx1, ny1 = shear_x(x1, y1, k)
nx2, ny2 = shear_x(x2, y2, k)

# Draw sheared line
draw_line(nx1, ny1, nx2, ny2, "red")

turtle.update()
turtle.done()
