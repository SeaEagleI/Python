class Point:
    row = 0
    col = 0
    def __init__(self,row,col):
        self.row = row
        self.col = col
        pass

#coding:utf-8
import pygame

def rect(Point,color):
    cell_width=W/COL
    cell_height=H/ROW  
    left=Point.col*cell_width
    top=Point.row*cell_height
    
    pygame.draw.rect(
            window, color,
            (left, top, cell_width, cell_height)
            )
    pass

pygame.init()
W=800
H=600

ROW=6
COL=8

size=(W,H)
window =pygame.display.set_mode(size)
pygame.display.set_caption('Snake')


bg_color=(255,255,255)


#Setting Cordinates
head=Point(row=int(ROW/2),col=int(COL/2))
head_color=(0,128,128)
food=Point(row=2,col=3)
food_color=(255,255,0)

#


#Game Loop
quit=True
clock=pygame.time.Clock()
while quit:
    #Handling Events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                quit=False
    
    
    #Rendering
    pygame.draw.rect(window,bg_color,(0,0,W,H))
    
    pygame.display.flip()
    
    #Print
    rect(head,head_color)
    rect(food,food_color)
    
    
    #Setting Frame Rate
    clock.tick(60)
    
#Ending Up





