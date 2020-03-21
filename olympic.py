# design olympic logo
from turtle import *
pensize(6)
r1=['blue','black','red']
for i in range(3):
    penup()
    pencolor(r1[i%3])
    goto(i*100,0)
    pendown()
    circle(45)
r2=["",'yellow','','green']
for i in range (1,4,2):
    penup()
    pencolor(r2[i])
    goto(i*55,-55)
    pendown()
    circle(50)
    
