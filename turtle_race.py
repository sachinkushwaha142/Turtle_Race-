from turtle import *
from random import *
title('Turtle Race')
#setup(1000,1000,0,0)
bgcolor('yellow')
#speed(10)
penup()
goto(-140,140)
for i in range(15):
    write(i,align='left')
    right(90)
    for j in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)
ada=Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,125)
ada.pendown()
for t in range(10):
    ada.right(36)

ada1=Turtle()
ada1.color('blue')
ada1.shape('turtle')
ada1.penup()
ada1.goto(-160,105)
ada1.pendown()
for t in range(10):
    ada1.left(36)

ada2=Turtle()
ada2.color('green')
ada2.shape('turtle')
ada2.penup()
ada2.goto(-160,85)
ada2.pendown()
for t in range(10):
    ada2.right(36)

ada3=Turtle()
ada3.color('black')
ada3.shape('turtle')
ada3.penup()
ada3.goto(-160,65)
ada3.pendown()
for t in range(10):
    ada3.left(36)

p1=0
p2=0
p3=0
p4=0
for i in range(100):
    r1=randint(1,5)
    p1+=r1
    ada.forward(r1)
    r2=randint(1,5)
    p2+=r2
    ada1.forward(r2)
    r3=randint(1,5)
    p3+=r3
    ada2.forward(r3)
    r4=randint(1,5)
    p4+=r3
    ada3.forward(r4)
    
l=[p1,p2,p3,p4]
winner=max(l)
if(winner==p1):
    write("red is winner",font=("Arial",10,"bold"))
elif(winner==p2):
        write("blue is winner",font=("Arial",10,"bold"))
elif(winner==p3):
        write("green is winner",font=("Arial",10,"bold"))
else:
    write("black is winner",font=("Arial",10,"bold"))

