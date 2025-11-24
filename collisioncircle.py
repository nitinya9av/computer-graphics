import turtle
import math
import time

turtle.Screen()
turtle.tracer(0)

def make_circle(x):
    t = turtle.Turtle()
    t.speed(0)
    t.color("black")
    t.penup()
    t.hideturtle()
    t.goto(x, -40)
    return t

c1, c2 = make_circle(-200), make_circle(200)
R = 40

def draw_circle(t):
    t.clear()
    t.pendown()
    t.circle(R)
    t.penup()

draw_circle(c1)
draw_circle(c2)

speed1, speed2 = 2, -2

while True:
    c1.goto(c1.xcor() + speed1, -R)
    c2.goto(c2.xcor() + speed2, -R)
    
    draw_circle(c1)
    draw_circle(c2)
    turtle.update()
    time.sleep(0.02)
    
    if math.dist((c1.xcor(), 0), (c2.xcor(), 0)) <= 2 * R:
        c1.color("red")
        c2.color("red")
        draw_circle(c1)
        draw_circle(c2)
        turtle.update()
        break

turtle.done()
