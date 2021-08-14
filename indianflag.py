import turtle as t

class flag:
    def __init__(self,a):
        self.a = a
        self.a.penup()

    def safron(self):
        self.a.goto(-300,200)
        self.a.pendown()
        self.a.color('orange')
        self.a.begin_fill()
        self.a.forward(600)
        self.a.right(90)
        self.a.forward(100)
        self.a.right(90)
        self.a.forward(600)
        self.a.right(90)
        self.a.forward(100)
        self.a.end_fill()
        self.a.penup()
    
    def sobuj(self):
        self.a.goto(-300,0)
        self.a.right(90)
        self.a.pendown()
        self.a.color('green')
        self.a.begin_fill()
        self.a.forward(600)
        self.a.right(90)
        self.a.forward(100)
        self.a.right(90)
        self.a.forward(600)
        self.a.right(90)
        self.a.forward(100)
        self.a.end_fill()
        self.a.penup()

    def cahkra(self):
        self.a.goto(50,50)
        self.a.pensize(5)
        self.a.pendown()
        self.a.color('blue')
        self.a.circle(49)
        self.a.penup()

    def spikes(self):
        self.a.goto(0,50)
        self.a.pensize(2)
        self.a.pendown()
        self.a.color('blue')
        # dx=-1
        for _ in range(29):
            self.a.forward(50)
            self.a.goto(0,50)
            self.a.right(25)
        self.a.penup()

        self.a.goto(0,-200)
        self.a.color('black')
        self.a.write('Happy Independence Day',align="center" ,font=("Helvatica",30,"normal"))
        self.a.hideturtle()

if __name__ == '__main__':
    obj=t.Turtle()
    o=flag(obj)
    o.safron()
    o.sobuj()
    o.cahkra()
    o.spikes()
    t.done()