import turtle

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for i in range(steps):
        turtle.penup()
        turtle.goto(x, y)
        turtle.dot(2, "black")   # draw a small pixel-like dot
        x += x_inc
        y += y_inc



# ---- USER INPUT ----
x1 = int(input("Enter starting x: "))
y1 = int(input("Enter starting y: "))
x2 = int(input("Enter ending x: "))
y2 = int(input("Enter ending y: "))

turtle.tracer(0)


dda_line(x1, y1, x2, y2)

turtle.done()
