import turtle as tu

class polygon:
    obj=tu.Turtle()
    def __init__(self,sides,length,color) -> None:
        self.n=sides
        self.len=length
        self.color=color
        angle=((self.n-2)/self.n)*180
        self.obj.color(self.color)
        self.obj.begin_fill()
        for _ in range(self.n):
            self.obj.forward(self.len)
            self.obj.left(180-angle)
        self.obj.end_fill()

polygon(5,200,'red')
tu.done()

