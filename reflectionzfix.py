import turtle

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

# Reflection about an axis perpendicular to XY-plane
# passing through fixed point (a, b)
def reflect_through_point(x, y, a, b):
    # shift point so that (a,b) becomes origin, apply reflection, shift back
    xr = - (x - a) + a
    yr = - (y - b) + b
    return xr, yr

# -------- USER INPUT --------
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

a = int(input("Enter fixed point a (x-coordinate): "))
b = int(input("Enter fixed point b (y-coordinate): "))

turtle.tracer(0)
turtle.hideturtle()

# Draw original line
draw_line(x1, y1, x2, y2, "black")

# Apply reflection through point (a, b)
nx1, ny1 = reflect_through_point(x1, y1, a, b)
nx2, ny2 = reflect_through_point(x2, y2, a, b)

# Draw reflected line in red
draw_line(nx1, ny1, nx2, ny2, "red")

turtle.update()
turtle.done()
