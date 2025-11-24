import turtle

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def draw_polygon(points, color):
    if not points: 
        return
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(points[0][0], points[0][1])
    turtle.pendown()
    for x, y in points[1:]:
        turtle.goto(x, y)
    turtle.goto(points[0][0], points[0][1])   # close polygon

# --------- Helper Functions for Clipping ---------
def inside(p, edge, xmin, xmax, ymin, ymax):
    x, y = p
    if edge == "LEFT":   return x >= xmin
    if edge == "RIGHT":  return x <= xmax
    if edge == "BOTTOM": return y >= ymin
    if edge == "TOP":    return y <= ymax

def intersection(p1, p2, edge, xmin, xmax, ymin, ymax):
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        m = None
    else:
        m = (y2 - y1) / (x2 - x1)

    if edge == "LEFT":
        x = xmin
        y = y1 + (xmin - x1) * m if m is not None else y1
        return (x, y)

    if edge == "RIGHT":
        x = xmax
        y = y1 + (xmax - x1) * m if m is not None else y1
        return (x, y)

    if edge == "BOTTOM":
        y = ymin
        if m is None:
            x = x1
        else:
            x = x1 + (ymin - y1) / m
        return (x, y)

    if edge == "TOP":
        y = ymax
        if m is None:
            x = x1
        else:
            x = x1 + (ymax - y1) / m
        return (x, y)


def clip_polygon(poly, edge, xmin, xmax, ymin, ymax):
    clipped = []
    n = len(poly)

    for i in range(n):
        p1 = poly[i]
        p2 = poly[(i + 1) % n]

        inside1 = inside(p1, edge, xmin, xmax, ymin, ymax)
        inside2 = inside(p2, edge, xmin, xmax, ymin, ymax)

        if inside1 and inside2:
            clipped.append(p2)
        elif inside1 and not inside2:
            clipped.append(intersection(p1, p2, edge, xmin, xmax, ymin, ymax))
        elif not inside1 and inside2:
            clipped.append(intersection(p1, p2, edge, xmin, xmax, ymin, ymax))
            clipped.append(p2)

    return clipped


# ------------------ USER INPUT --------------------
n = int(input("Enter number of polygon vertices: "))

poly = []
for i in range(n):
    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))
    poly.append((x, y))

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

# Draw original polygon
draw_polygon(poly, "black")

# Apply Sutherland–Hodgman (clip against 4 edges)
for edge in ["LEFT", "RIGHT", "BOTTOM", "TOP"]:
    poly = clip_polygon(poly, edge, xmin, xmax, ymin, ymax)

# Draw clipped polygon
draw_polygon(poly, "red")

turtle.update()
turtle.done()
