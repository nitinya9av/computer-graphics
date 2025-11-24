import turtle

def draw_point(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(5, color)

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def translate_point(x, y, tx, ty):
    return x + tx, y + ty


# ---- USER INPUT ----
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

tx = int(input("Enter translation Tx: "))
ty = int(input("Enter translation Ty: "))

# Fast drawing
turtle.tracer(0)
turtle.hideturtle()

# Draw original line (Black)
draw_line(x1, y1, x2, y2, "black")

# Apply translation
nx1, ny1 = translate_point(x1, y1, tx, ty)
nx2, ny2 = translate_point(x2, y2, tx, ty)

# Draw translated line (Red)
draw_line(nx1, ny1, nx2, ny2, "red")
turtle.update()

turtle.done()
