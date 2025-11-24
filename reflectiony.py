import turtle

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def reflect_y(x, y):
    return -x, y   # reflection about y-axis


# ---- USER INPUT ----
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter x2: "))

turtle.tracer(0)
turtle.hideturtle()

# Draw original line
draw_line(x1, y1, x2, y2, "black")

# Reflection about Y-axis
nx1, ny1 = reflect_y(x1, y1)
nx2, ny2 = reflect_y(x2, y2)

# Draw reflected line in red
draw_line(nx1, ny1, nx2, ny2, "red")

turtle.update()
turtle.done()
