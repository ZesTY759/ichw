import math
import turtle

def aspect(turtle,size,k):
    if size < 1:
        turtle.hideturtle()
    colors=['yellow', 'blue', 'orange', 'gray', 'brown']
    turtle.shape("circle")
    turtle.shapesize(size,size,1)
    turtle.color(colors[k])
    turtle.speed(10)

def track(turtle,r1,r2,m,n,d):
    if m == 0:
        turtle.up()
        turtle.goto(r1*math.cos(math.radians(1))+d,r2*math.sin(math.radians(1)))
        turtle.down()
        turtle.showturtle()
    else:
        m = m/n
        turtle.goto(r1*math.cos(math.radians(m))+d,r2*math.sin(math.radians(m)))

wn=turtle.Screen()
wn.bgcolor("black")
mer=turtle.Turtle() 
aspect(mer,0.2,2)
ven=turtle.Turtle()
aspect(ven,0.3,3)
ear=turtle.Turtle() 
aspect(ear,0.3,1)
mar=turtle.Turtle()
aspect(mar,0.2,4)
jup=turtle.Turtle() 
aspect(jup,0.6,3)
sat=turtle.Turtle() 
aspect(sat,0.6,4)
sun=turtle.Turtle() 
aspect(sun,1.2,0)

for i in range(3000):
    track(mer,26,18,i,0.1,-4)
    track(ven,45,44.5,i,0.2,0)
    track(ear,62.5,61,i,0.3,0)
    track(mar,100,83,i,0.6,9)
    track(jup,190,172,i,0.9,15)
    track(sat,280,254,i,1.8,22)
    
