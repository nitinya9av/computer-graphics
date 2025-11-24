import turtle

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    x, y = x1, y1

    if dx > dy:
        p = 2 * dy - dx
        for i in range(dx):
            turtle.penup()
            turtle.goto(x, y)
            turtle.dot(2, "black")

            if p >= 0:
                y += sy
                p -= 2 * dx
            x += sx
            p += 2 * dy
    else:
        p = 2 * dx - dy
        for i in range(dy):
            turtle.penup()
            turtle.goto(x, y)
            turtle.dot(2, "black")

            if p >= 0:
                x += sx
                p -= 2 * dy
            y += sy
            p += 2 * dx


# ---- USER INPUT ----
x1 = int(input("Enter starting x: "))
y1 = int(input("Enter starting y: "))
x2 = int(input("Enter ending x: "))
y2 = int(input("Enter ending y: "))

# Fast drawing like your DDA code
turtle.tracer(0)

bresenham_line(x1, y1, x2, y2)
    
turtle.done()
