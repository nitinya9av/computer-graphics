import turtle

def plot_points(xc, yc, x, y):
    turtle.penup()

    turtle.goto(xc + x, yc + y)
    turtle.dot(2, "black")

    turtle.goto(xc - x, yc + y)
    turtle.dot(2, "black")

    turtle.goto(xc + x, yc - y)
    turtle.dot(2, "black")

    turtle.goto(xc - x, yc - y)
    turtle.dot(2, "black")


def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry

    # Region 1 decision parameter
    p1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx)

    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    # -------- REGION 1 --------
    while dx < dy:
        plot_points(xc, yc, x, y)

        x += 1
        dx = 2 * ry * ry * x

        if p1 < 0:
            p1 += dx + (ry * ry)
        else:
            y -= 1
            dy = 2 * rx * rx * y
            p1 += dx - dy + (ry * ry)

    # Region 2 decision parameter
    p2 = (ry*ry) * ((x + 0.5)**2) + (rx*rx) * ((y - 1)**2) - (rx*rx * ry*ry)

    # -------- REGION 2 --------
    while y >= 0:
        plot_points(xc, yc, x, y)

        y -= 1
        dy = 2 * rx * rx * y

        if p2 > 0:
            p2 -= dy + (rx * rx)
        else:
            x += 1
            dx = 2 * ry * ry * x
            p2 += dx - dy + (rx * rx)


# ---- USER INPUT ----
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
rx = int(input("Enter x-radius (rx): "))
ry = int(input("Enter y-radius (ry): "))

turtle.tracer(0)

midpoint_ellipse(xc, yc, rx, ry)

turtle.done()
