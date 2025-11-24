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

earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.shapesize(0.5)
earth.penup()

orbit_radius = 150
angle = 0

while True:
    x = orbit_radius * math.cos(math.radians(angle))
    y = orbit_radius * math.sin(math.radians(angle))
    
    earth.goto(x, y)
    turtle.update()
    time.sleep(0.02)
    
    angle += 1
    if angle >= 360:
        angle = 0

turtle.done()