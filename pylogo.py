import turtle as t

class logo:

    def __init__(i,t) -> None:
        i.t=t

    def neel(i):
        i.t.penup()
        i.t.pencolor('blue')
        # i.t.goto(-100,0)
        i.t.pendown()
        i.t.left(90)
        i.t.forward(100)
        i.t.right(90)
        i.t.forward(50)
        i.t.right(90)
        i.t.forward(100)
        i.t.right(90)
        i.t.forward(50)
        i.t.right(90)
        i.t.forward(50)
        pass

    def holud(i):
        i.t.penup()
        i.t.pencolor('yellow')
        i.t.goto(-100,0)
        
        pass

if __name__ =="__main__":
    t.Turtle()
    obj=logo(t)
    obj.neel()
    obj.holud()
    t.done()