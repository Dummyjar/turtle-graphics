import math
import webbrowser
import time
import turtle as t
class LOVE:
    def __init__(self,curve,s) -> None:
        self.lou=curve
        self.lou.pendown()
        self.lou.color('red')
        self.lou.begin_fill()
        for i in range(372):
            x=16*((math.sin(math.radians(i)))*(math.sin(math.radians(i)))*(math.sin(math.radians(i))))
            y=13*(math.cos(math.radians(i)))-5*(math.cos(2*(math.radians(i))))-2*(math.cos(3*(math.radians(i))))-math.cos(4*(math.radians(i)))
            self.lou.goto(s*x,s*y)
        self.lou.penup()    
        self.lou.end_fill()
        self.lou.hideturtle()
if __name__ == "__main__":
    win = t.Screen()
    url="https://www.youtube.com/watch?v=izGwDsrQ1eQ"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    time.sleep(3)
    win.title("TURU L0B")
    caption=t.Turtle()
    caption.color('red')
    caption.penup()
    caption.goto(0,250)
    caption.write("Hey Senorita! You're iota. I'm iota.\nTogether we can make it REAL.",align="center" ,font=("Helvatica",20,"normal"))
    caption.penup()
    caption.hideturtle()
    love= t.Turtle()
    LOVE(love,10)
    t.done()
