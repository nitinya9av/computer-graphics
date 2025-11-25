import turtle

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def inside(x, y, xmin, xmax, ymin, ymax):
    return xmin <= x <= xmax and ymin <= y <= ymax

def clip_midpoint(x1, y1, x2, y2, xmin, xmax, ymin, ymax, depth=0):

    if depth > 25:     # prevent infinite recursion
        return None

    p1_inside = inside(x1, y1, xmin, xmax, ymin, ymax)
    p2_inside = inside(x2, y2, xmin, xmax, ymin, ymax)

    # Case 1: fully inside
    if p1_inside and p2_inside:
        return x1, y1, x2, y2

    # Case 2: both outside AND on the same outside region? reject
    if not p1_inside and not p2_inside:
        # Check trivial rejection using outcodes (fast)
        code1 = (x1 < xmin) | ((x1 > xmax) << 1) | ((y1 < ymin) << 2) | ((y1 > ymax) << 3)
        code2 = (x2 < xmin) | ((x2 > xmax) << 1) | ((y2 < ymin) << 2) | ((y2 > ymax) << 3)
        if code1 & code2:
            return None

    # Subdivide midpoint
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    # Recurse on left half
    left = clip_midpoint(x1, y1, mx, my, xmin, xmax, ymin, ymax, depth + 1)

    # Recurse on right half
    right = clip_midpoint(mx, my, x2, y2, xmin, xmax, ymin, ymax, depth + 1)

    # Combine valid segments
    if left and right:
        return left[0], left[1], right[2], right[3]
    elif left:
        return left
    elif right:
        return right
    else:
        return None


# ------------------ USER INPUT --------------------
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter x2: "))

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

# Apply Midpoint Subdivision Clipping
result = clip_midpoint(x1, y1, x2, y2, xmin, xmax, ymin, ymax)

# Draw clipped line (if any)
if result:
    nx1, ny1, nx2, ny2 = result
    draw_line(nx1, ny1, nx2, ny2, "red")

turtle.update()
turtle.done()
