from turtle import *
pencolor('blue')
color=['blue','green','red','yellow','orange','purple']

for i in range (500):
    pencolor(color[i%6])
    width(i/100+1)
    forward(i)
    left(59)
    
   
