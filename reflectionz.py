import turtle


# Function to draw a line
def draw_line(p1, p2, color):
    turtle.color(color)
    turtle.penup()
    turtle.goto(p1)
    turtle.pendown()
    turtle.goto(p2)

# Reflection about Z-axis (x→−x, y→−y)
def reflect_Z(p):
    return (-p[0], -p[1])

# ---- USER INPUT ----
print("Enter coordinates of the line:")
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

turtle.tracer(0)
turtle.hideturtle()

P1 = (x1, y1)
P2 = (x2, y2)

# Reflected points
R1 = reflect_Z(P1)
R2 = reflect_Z(P2)

# Draw original (RED)
draw_line(P1, P2, "red")

# Draw reflected (BLUE)
draw_line(R1, R2, "blue")

turtle.update()
turtle.done()
