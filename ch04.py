#%% first cell
money,c500,c100,c50,c10=0,0,0,0,0

money=int(input("교환할 돈은 얼마?"))

c500=money//500
money%=500

c100=money//100
money%=100

c50=money//50
money%=50

c10=money //10
money%=10

print("\n 500원짜리 ==> %d개" % c500)
print("100 원짜리 ==> %d개" %c100)
print("50원짜리 ==> %d개"%c50)
print("10원짜리 ==> %d개"%c10)
print("바꾸지 못한 잔돈 ==> %d원\n"%money)
#%% second cell
import turtle
import random

swidth,sheight,pSize,exitCount=300,300,3,0
r,g,b,angle,dist,curX,curY=[0]*7

turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidth+30,height=sheight+30)
turtle.screensize(swidth,sheight)

while True:
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor((r,g,b))
    
    angle=random.randrange(0,360)
    dist=random.randrange(1,100)
    turtle.left(angle)
    turtle.forward(dist)
    curX=turtle.xcor()
    curY=turtle.ycor()
    
    if(-swidth/2 <=curX and curX <=swidth/2) and (-sheight/2 <= curY and curY<=sheight/2):
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        
        exitCount+=1
        if exitCount >=5:
            break
        
turtle.done()