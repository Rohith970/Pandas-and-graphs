# Square Spiral
import turtle as t
a1=t.Turtle()

for i in range (500):
    if i%3==0:
        a1.pencolor('blue')
        a1.forward(i)
    elif  i%3==1:
        a1.pencolor('orange')
        a1.forward(i)
    else:
        a1.pencolor('green')
        a1.forward(i)
    
    a1.right(91)
t.done()
