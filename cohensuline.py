import turtle

# Region codes
INSIDE = 0
LEFT   = 1
RIGHT  = 2
BOTTOM = 4
TOP    = 8

def compute_code(x, y, xmin, xmax, ymin, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def cohen_sutherland_clip(x1, y1, x2, y2, xmin, xmax, ymin, ymax):

    code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)
    code2 = compute_code(x2, y2, xmin, xmax, ymin, ymax)

    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, xmax, ymin, ymax)

    if accept:
        return x1, y1, x2, y2
    else:
        return None


# ------------------ USER INPUT -------------------
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

xmin = int(input("Enter xmin: "))
ymin = int(input("Enter ymin: "))
xmax = int(input("Enter xmax: "))
ymax = int(input("Enter ymax: "))

turtle.tracer(0)
turtle.hideturtle()

# Draw clipping window
draw_line(xmin, ymin, xmax, ymin, "blue")
draw_line(xmax, ymin, xmax, ymax, "blue")
draw_line(xmax, ymax, xmin, ymax, "blue")
draw_line(xmin, ymax, xmin, ymin, "blue")

# Draw original line
draw_line(x1, y1, x2, y2, "black")

# Clip the line
result = cohen_sutherland_clip(x1, y1, x2, y2, xmin, xmax, ymin, ymax)

# Draw clipped line
if result:
    nx1, ny1, nx2, ny2 = result
    draw_line(nx1, ny1, nx2, ny2, "red")

turtle.update()
turtle.done()
