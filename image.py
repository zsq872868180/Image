
import turtle
p = turtle.Pen( )
p.penup( )
p.goto(0, -200)
p.setheading(90)
p.pensize(7)
p.pencolor('green')
p.pendown( )
 

def branch(plist, len):
    if (len > 15):
        list = []
        for p in plist:
            p.forward(len)
            q = p.clone( )
            p.left(65)
            q.right(65)
            list.append(p)
            list.append(q)
        branch(list, len * 0.65)
 
         
branch([p], 200)
turtle.done( )
