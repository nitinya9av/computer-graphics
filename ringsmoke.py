import turtle
import time

turtle.tracer(0)

def ring_of_smoke(x, y, max_radius, num_circles):
    turtles = [turtle.Turtle() for _ in range(num_circles)]
    for t in turtles:
        t.hideturtle()
        t.speed(0)
        t.pensize(2)
    
    radii = [5] * num_circles
    delays = [i * 20 for i in range(num_circles)]
    step = 0
    
    while any(r <= max_radius + 3 for r in radii):
        for i, t in enumerate(turtles):
            if step >= delays[i]:
                if radii[i] <= max_radius:
                    t.clear()
                    t.penup()
                    t.goto(x - radii[i], y)
                    t.pendown()
                    t.setheading(90)
                    for _ in range(2):
                        t.circle(radii[i], 90)
                        t.circle(radii[i] * 0.3, 90)
                    radii[i] += 3
                else:
                    t.clear()
        
        turtle.update()
        step += 1
        time.sleep(0.03)
    
    for t in turtles:
        t.clear()
    turtle.update()

ring_of_smoke(0, 0, 150, 10)
turtle.done()
