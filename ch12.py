# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:38:05 2020

@author: Young Hun Park
"""
#%% 1
class Car:
    color=""
    speed=0
    
    def upSpeed(self,value):
        self.speed+=value
    def downSpeed(self,value):
        self.speed-=value
    
myCar1=Car()
myCar1.color="빨강"
myCar1.speed=0

myCar2=Car()
myCar2.color="파랑"
myCar2.speed=0

myCar3=Car()
myCar3.color="노랑"
myCar3.speed=0

myCar1.upSpeed(30)

print("자동차 1의 색상 %s, 속도:%dkm"%(myCar1.color,myCar1.speed))

#%% 2
class Car:
    color=""
    speed=0
    
    def __init__(self):
        self.color="빨강"
        self.speed=0
        
    def upSpeed(self,value):
        self.speed+=value
        
    def downSpeed(self,value):
        self.speed-=value
        

myCar1=Car()
myCar2=Car()

print(myCar1.color,myCar1.speed)
print(myCar2.color,myCar2.speed)

#%% 3
class Car:
    color=""
    speed=0
    
    def __init__(self,value1,value2):
        self.color=value1
        self.speed=value2
        
    
myCar1=Car("빨강",30)
myCar2=Car("파랑",60)

print(myCar1.color,myCar1.speed)
print(myCar2.color,myCar2.speed)
#%%  4
class Car:
    name=""
    speed=0
    
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
        
    def getName(self):
        return self.name
    def getSpeed(self):
        return self.speed
    
car1,car2=None,None

car1=Car("아우디",0)
car2=Car("벤츠",30)

print(car1.name,car1.speed)
print(car2.name,car2.speed)

#%% 5

class Car:
    speed=0
    def upSpeed(self,value):
        self.speed+=value
        
        print("현재 속도(슈퍼 클래스):%d"%self.speed)
        
class Sedan(Car):
    def upSpeed(self,value):
        self.speed+=value
        
        if self.speed>150:
            self.speed=150
        print(self.speed)
        
class Truck(Car):
    pass

sedan1,truck1=None,None

truck1=Truck()
sedan1=Sedan()

print("트럭-->",end="")
truck1.upSpeed(200)

print("승용치-->",end="")
sedan1.upSpeed(200)

#%% 6

import turtle
import random

class Shape:
    myTurtle=None
    cx,cy=0,0
    
    def __init__(self):
        self.myTurtle=turtle.Turtle('turtle')
    
    def setPen(self):
        r=random.random()
        g=random.random()
        b=random.random()
        self.myTurtle.pencolor((r,g,b))
        pSize=random.randrange(1,10)
        self.myTurtle.pensize(pSize)
        
    def drawShape(self):
        pass
    
class Rectangle(Shape):
    width,height=[0]*2
    
    def __init__(self,x,y):
        Shape.__init__(self)
        self.cx=x
        self.cy=y
        self.width=random.randrange(20,100)
        self.height=random.randrange(20,100)
        
    def drawShape(self):
        sx1,sy1,sx2,sy2=[0]*4
        
        sx1=self.cx-self.width/2
        sy1=self.cy-self.height/2
        sx2=self.cx+self.width/2
        sy2=self.cy+self.height/2
        
        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(sx1,sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1,sy2)
        self.myTurtle.goto(sx2,sy2)
        self.myTurtle.goto(sx2,sy1)
        self.myTurtle.goto(sx1,sy1)
        
        
def screenLeftClick(x,y):
    rect=Rectangle(x,y)
    rect.drawShape()
    
turtle.title('거북이로 객체지향 사각형 s그리기')
turtle.onscreenclick(screenLeftClick,1)
turtle.done()
#%% 7

class Line:
    length=0
    
    def __init__(self,length):
        self.length=length
        print(self.length,'길이의 선이 생성되었습니다')
        
    def __del__(self):
        print(self.length,'길이의 선이 삭제되었습니다.')
        
    def __repr__(self):
        return '선의 길이:'+str(self.length)
    
    def __add__(self,other):
        return self.length + other.length
    
    def __lt__(self,other):
        return self.length<other.length
    
    def __eq__(self,other):
        return self.length==other.length
    
myLine1=Line(100)
myLine2=Line(200)

print(myLine1)

print('두 선의 길이 합:',myLine1+myLine2)

if myLine1<myLine2:
    print('선분2가 더기네요')
elif myLine1==myLine2:
    print('두 선분이 같네요')
else:
    print('모르겠네요')

del(myLine1)

#%% 8
class SuperClass:
    def method(self):
        pass
class SubClass1(SuperClass):
    def method(self):
        print("Subclass1에서 method()를 오버라이딩함")
    
class SubClass2(SuperClass):
    pass

sub1=SubClass1()
sub2=SubClass2()

sub1.method()
sub2.method()

# %%9

import time

class RacingCar:
    carName=''
    
    def __init__(self,name):
        self.carName=name
    
    def runCar(self):
        for _ in range(0,3):
            carStr=self.carName+'~달립니다.\n'
            print(carStr,end='')
            time.sleep(0.1)

car1=RacingCar('@자동차1')
car2=RacingCar('#자동차2')
car3=RacingCar('$자동차3')

car1.runCar()
car2.runCar()
car3.runCar()

# %%10
import threading
import time

th1=threading.Thread(target=car1.runCar)
th2=threading.Thread(target=car2.runCar)
th3=threading.Thread(target=car3.runCar)

th1.start()
th2.start()
th3.start()

#%% 11
import multiprocessing

class RacingCar:
    carName=''
    
    def __init__(self,name):
        self.carName=name
    
    def runCar(self):
        for _ in range(0,3):
            carStr=self.carName+'~달립니다.\n'
            print(carStr,end='')
            time.sleep(0.1)
            
if __name__=="__main__":
    car1=RacingCar('@자동차1')
    car2=RacingCar('#자동차2')
    car3=RacingCar('$자동차3')
    
    mp1=multiprocessing.Process(target=car1.runCar)
    mp2=multiprocessing.Process(target=car2.runCar)
    mp3=multiprocessing.Process(target=car3.runCar)
    
    mp1.start()
    mp2.start()
    mp3.start()
    
    mp1.join()
    mp2.join()
    mp3.join()
    
#%% 12
    
from tkinter import *
from tkinter.ttk import *
import random
import time
import threading

class ThreadProgressBar():
    thread=None
    progress=None
    
    def __init__(self,parent):
        self.progress=Progressbar(parent,orient=HORIZONTAL,length=500)
        self.progress.pack(side=TOP,fill=X,ipadx=10,padx=10,pady=10)
        self.thread=threading.Thread(target=self.runProgress,args=(self,progress,))
        self.thread.start()
    
    def runProgress(self,progress):
        hop=0
        while True:
            hop=random.randrange(0,10)
            if progress['value']>=100:
                break
            progress['value']+=hop
            time.sleep(0.5)
    
    def runThreadProgress():
        thBar1=ThreadProgressBar(window)
        thBar2=ThreadProgressBar(window)
        thBar3=ThreadProgressBar(window)
        
    if __name__=="__main__":
        window=Tk()
        window.geometry("300x250")
        window.title('멀티 쓰레드')
        threadtButton=Button(window,text='멀티 쓰레드 시작',command=runThreadProgress)
        threadtButton.pack(side=TOP,fil=X,ipadx=10,ipady=10,padx=10,pady=10)
        
        window.mainloop()
        
#%% 9
from tkinter import *
import math
import random

class Shape:
    color,width='',0
    shX1,shY1,shX2,shY2=[0]*4
    def drawShape(self):
        raise NotImplementedError()
    
class Rectangle(Shape):
    objects=None
    
    def __init__(self,x1,y1,x2,y2,c,w):
        self.shX1=x1
        self.shY1=y1
        self.shX2=x2
        self.shY2=y2
        self.color=c
        self.width=w
        self.drawShape()
        
    def __del__(self):
        for obj in self.objects:
            canvas.delete(obj)
            
    def drawShape(self):
        sx1=self.shX1; sy1=self.shY1; sx2=self.shX2; sy2=self.shY2
        squreList=[]
        squreList.append(canvas.create_line(sx1,sy1,sx1,sy2,fill=self.color,width=self.width))
        squreList.append(canvas.create_line(sx1,sy2,sx2,sy2,fill=self.color,width=self.width))
        squreList.append(canvas.create_line(sx2,sy2,sx2,sy1,fill=self.color,width=self.width))
        squreList.append(canvas.create_line(sx2,sy1,sx1,sy1,fill=self.color,width=self.width))
        
        self.objects=squreList
        
class Circle(Shape):
    objects=None
    def __init__(self,x1,y1,x2,y2,c,w):
        self.shX1=x1
        self.shY1=y1
        self.shX2=x2
        self.shY2=y2
        self.color=c
        self.width=w
        self.drawShape()
        
    def __del__(self):
        canvas.delete(self.objects)
        
    def drawShape(self):
        sx1=self.shX1; sy1=self.shY1; sx2=self.shX2; sy2=self.shY2
        self.objects=canvas.create_oval(sx1,sy1,sx2,sy2,outline=self.color,width=self.width)
        
def getColor():
    r=random.randrange(16,256)
    g=random.randrange(16,256)
    b=random.randrange(16,256)
    
    return "#" +hex(r)[2:]+hex(g)[2:]+hex(b)[2:]

def getWidth():
    return random.randrange(1,9)

def startDrawRect(event):
    global x1,y1,x2,y2,shapes
    x1=event.x
    y1=event.y
    
def endDrawRect(event):
    global x1,y1,x2,y2,shapes
    x2=event.x
    y2=event.y
    rect=Rectangle(x1,y1,x2,y2,getColor(),getWidth())
    shapes.append(rect)

def startDrawCircle(event):
    global x1,y1,x2,y2,shapes
    x1=event.x
    y1=event.y

def endDrawCircle(event):
    global x1,y1,x2,y2,shapes
    x2=event.x
    y2=event.y
    cir=Circle(x1,y1,x2,y2,getColor(),getWidth())

def deleteShape(event):
    global shapes
    if len(shapes) !=0:
        shp=shapes.pop()
        del(shp)
    
shapes=[]
window=None
canvas=None
x1,y1,x2,y2=None,None,None,None

if __name__=="__main__":
    window=Tk()
    window.title('객체지향 그림판')
    canvas=Canvas(window,height=300,width=300)
    canvas.bind("<Button-1>",startDrawRect)
    canvas.bind("<ButtonRelease-1>",endDrawRect)
    canvas.bind("<Button-2>",deleteShape)
    canvas.bind("<Button-3>",startDrawCircle)
    canvas.bind("<ButtonRelease-3>",endDrawCircle)
    
    canvas.pack()
    window.mainloop()
         