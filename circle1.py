from turtle import *
i=0
pencolor('blue')
color=['blue','orange','green','red','purple']
for i  in range(100):
    pencolor(color[i%6])
    circle(10*i)
    up()
    sety((10*i)*(-1))
    down()
    i=i+1;
    
