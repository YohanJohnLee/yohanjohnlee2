from turtle import *
from math import *
import turtle as t
t.shape ("circle")
import random
 
a=200
b=200
 
speed(0)
 
penup()
r = sqrt(a*a-b*b)
goto(r,0)
degree = random.randrange(1,360)
setheading(degree)
 
print(heading())
 
def collision(x1,y1,x2,y2):
  h = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
  a1 = (a*a*y2)/(x2*b*b)
  b1 = y2+x2*-1*a1
  d=abs((a1*(x1-x2)+y2-x1)/(sqrt(a1*a1+b1*b1)))
  theta = acos(h/d)
  dg = theta*360/2*pi
  dg = 180 - 2*dg
  return dg
 
pendown()
 
while(1):
  for i in range(0,1020):
    forward(0.1)
    pos = position()
    x = pos[0]
    y = pos[1]
    if(b*b*x*x + a*a*y*y >= a*a*b*b):
      cx = x
      cy = y
      turn = collision(x,y,cx,cy)
      left(turn)
      break
