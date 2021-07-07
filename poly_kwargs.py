import turtle

class poly:

    def __init__(self,**k) -> None:
        self.side=k['side']
        self.size=k['size']
        self.color=k['color']
        self.interior_angles=(self.side-2)*180
        self.angle=self.interior_angles/self.side

    def draw(self):
        turtle.color(self.color)
        for i in range(self.side):
            turtle.forward(self.size)
            turtle.right(180-self.angle)
        turtle.done()
# poly(side,size,color)
sq=poly(side=6,size=100,color='red')
sq.draw()

