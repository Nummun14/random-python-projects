import turtle
import time

# Create two turtles
t = turtle.Turtle()
t2 = turtle.Turtle()

# Move the turtles to their starting positions
t.pu()
t.goto(-50, 25)
t2.pu()
t2.goto(-50, -25)

# Put the turtles' pens down
t.pd()
t2.pd()

# Draw three sides of each triangle
for i in range(3):
    t.fd(100)
    t.rt(120)
    t2.fd(100)
    t2.lt(120)
time.sleep(5)
