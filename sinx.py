import math
import turtle

class trigo:

    def __init__(self,turt) -> None:
        self.curve=turt
        

    def sinx(self,size,span,start_x=0,amplitude=1):  
        self.curve.goto(start_x,y=0)
        self.curve.pendown()
        for i in range(start_x,span):
            a=math.radians(i)
            b=(amplitude)*(math.sin(math.radians(i)))
            self.curve.goto(size * a,size * b)
        self.curve.penup()
        
    def cosx(self,size,span,start_x=0,amplitude=1,color='black'):  
        self.curve.penup()
        
        
        self.curve.sety((amplitude)*(math.cos(math.radians(start_x))))
        self.curve.color(color)
        self.curve.pendown()
        for i in range(start_x,span):
            a=math.radians(i)
            b=(amplitude)*(math.cos(math.radians(i)))
            self.curve.goto(size * a,size * b)
        self.curve.penup()
    
        

if __name__=="__main__":
    j=turtle.Turtle()
    obj=trigo(j)
    
    obj.cosx(40,700,color='red')
    turtle.done()