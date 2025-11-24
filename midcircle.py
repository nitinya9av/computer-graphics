import turtle

def plot_circle_points(xc, yc, x, y):
    turtle.penup()

    turtle.goto(xc + x, yc + y)
    turtle.dot(2, "black")

    turtle.goto(xc - x, yc + y)
    turtle.dot(2, "black")

    turtle.goto(xc + x, yc - y)
    turtle.dot(2, "black")

    turtle.goto(xc - x, yc - y)
    turtle.dot(2, "black")

    turtle.goto(xc + y, yc + x)
    turtle.dot(2, "black")

    turtle.goto(xc - y, yc + x)
    turtle.dot(2, "black")

    turtle.goto(xc + y, yc - x)
    turtle.dot(2, "black")

    turtle.goto(xc - y, yc - x)
    turtle.dot(2, "black")


def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r    # Initial decision parameter

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        plot_circle_points(xc, yc, x, y)


# ---- USER INPUT ----
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r  = int(input("Enter radius: "))

# Fast drawing like your other codes
turtle.tracer(0)

midpoint_circle(xc, yc, r)

turtle.done()
