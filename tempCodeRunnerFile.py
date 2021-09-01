import numpy as np
import pygame
from pygame.locals import *

class trig:
    Ys=[] # to collect all the ordinates
    def __init__(self,width=1600,height=900,gap=100,fps=60,radius=100):
        self.width=width # width of the window
        self.height=height # height of the window
        self.fps=fps # frame rate per second
        self.screen=pygame.display.set_mode((self.width,self.height)) 
        # setting the screen dimensions
        self.clock=pygame.time.Clock()
        self.gap=gap # the distance between the radius
        #  pointer and the starting point of the curve
        self.t=0 # the will be the x axis
        self.r=radius #  length of the radius of the circle
  
        self.run=True
        while self.run:
            self.clock.tick(self.fps)
            self.screen.fill('white') # filling the whole canvas with white background
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run= False
            if event.type == KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()

            x,y=400,400 # center of the circle

            x+=(self.r * np.cos(self.t)) 
            y+=(self.r * np.sin(self.t))
            pygame.draw.line(self.screen, 'grey', (400,400), (400+1000, 400), 3)
             # this will create a horizontal line

            pygame.draw.line(self.screen, 'grey', (400,400+self.r), (400+1000, 400+self.r), 3)
             # this will create a horizontal line above the circle
            pygame.draw.line(self.screen, 'grey', (400,400-self.r), (400+1000, 400-self.r), 3)
             # this will create a horizontal line below the circle
            pygame.draw.circle(self.screen,'blue',(400,400),self.r,5) 
            # this will create a circle with center (400,400)
            pygame.draw.line(self.screen,'green',(400,400),(x,y),3)
             #this will draw the radius of the circle
            
            self.Ys.insert(0,y)# inserting the y values at the begining of the Ys list
            
            if len(self.Ys) >1100 - self.gap:self.Ys.pop() 
            # this will restrict the length of the Ys to a certain limit

            pygame.draw.line(self.screen, 'black', (x,y), (400+self.gap, self.Ys[0]), 3)
            # this will create the joining line between the curve and the circle's radius
             
            for i in range(len(self.Ys)):
                pygame.draw.circle(self.screen,'red',(i+400+self.gap,self.Ys[i]),1,1)
                # this will create the sin curve 
                # it will create bunch of small circles with varying centers in such a 
                # way that it will trajectory of the centers of all those small circles
                # will give rise to a sine curve
                
            if event.type==KEYDOWN:
                if event.key==K_RIGHT:
                    self.gap+=1
                if event.key==K_LEFT:
                    self.gap-=1
             # this part of code gives the user the freedom to set the speed of the 
             # animation and also set the gap between the circle and the sine curve
                    
            self.t+=0.01
            pygame.display.update()

if __name__ == '__main__':
    sin=trig()
    pygame.quit()