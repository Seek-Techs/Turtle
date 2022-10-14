import turtle
import time
fortify = turtle.Turtle()
x = 0
y = 0
fortify.home()
fortify.write((x, y))
y = -100
fortify.speed(0)
fortify.penup()
fortify.goto(x, y)
fortify.pendown()
fortify.begin_fill()
fortify.fillcolor("red")
fortify.circle(100)
fortify.penup()
fortify.home()
y = -60
fortify.home()
fortify.goto(x, y)
fortify.pendown()
fortify.circle(60)
fortify.end_fill()
fortify.penup()
fortify.home()

fortify.left(90)
for i in range(12):
    fortify.right(360/12)
    fortify.forward(79)
    fortify.write((i + 1))
    fortify.goto(0,0)

def draw_hour_arm():
    fortify.penup()
    fortify.home()
    fortify.right(180)
    fortify.pendown()
    fortify.pensize(5)
    fortify.forward(40)

def draw_minute_arm():
    fortify.penup()
    fortify.home()
    fortify.right(270)
    fortify.pendown()
    fortify.pensize(3)
    fortify.forward(70)

draw_hour_arm()
draw_minute_arm()

fortify.pensize(2)
angle1 = 0
while True:
    start = time.time()
    first_start = 1
    if first_start == 1:
        fortify.penup()
        fortify.home()
        fortify.left(90)
        first_start = 2
    fortify.right(angle1)
    fortify.pendown()
    fortify.forward(60)
    time.sleep(1- (time.time() - start))
    fortify.undo()
    fortify.penup()
    fortify.goto(0,0)
    angle1 += (360/60)
turtle.done()