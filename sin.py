import turtle as t
import math
chompa=t.Turtle()
chompa.speed(0)
s=20
a=1
for i in range(1500):
    x=math.radians(i)
    y=(a)*(math.sin(math.radians(i)))
    chompa.goto(s*x,s*y)


t.done()