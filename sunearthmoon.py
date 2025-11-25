import turtle
import math
import time

turtle.tracer(0)
screen = turtle.Screen()
screen.bgcolor("black")

sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.penup()
sun.shapesize(2)
sun.goto(0, 0)

earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.shapesize(0.5)
earth.penup()

moon = turtle.Turtle()
moon.shape("circle")
moon.color("grey")
moon.shapesize(0.2)
moon.penup()

orbit_radius = 150
angle = 0

moon_orbit_radius = 40
moon_angle = 0

while True:
    # Earth position around Sun
    x = orbit_radius * math.cos(math.radians(angle))
    y = orbit_radius * math.sin(math.radians(angle))
    earth.goto(x, y)

    # Moon position relative to Earth
    mx = x + moon_orbit_radius * math.cos(math.radians(moon_angle))
    my = y + moon_orbit_radius * math.sin(math.radians(moon_angle))
    moon.goto(mx, my)

    turtle.update()
    time.sleep(0.02)

    angle = (angle + 1) % 360
    moon_angle = (moon_angle + 5) % 360

turtle.done()