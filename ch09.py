# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:59:08 2020

@author: Young Hun Park
"""

coffe=0
#%% 1
def plus(v1,v2):
    
    result=0
    result=v1+v2
    return result

hap=0

hap=plus(100,200)
print(hap)

#%% 2

def calc(v1,v2,op):
    result=0
    
    if op=='+':
        result=v1+v2
    elif op =='-':
        result=v1-v2
    elif op=='*':
        result=v1*v2
    elif op=='/':
        result=v1/v2
    
    return result

res=0
var1,var2,oper=0,0,""

oper=input("계산을 입력하세요:")
var1=int(input("첫 번째 수를 입력하세요:"))
var2=int(input("두 번째 수를 입력하세요:"))

res=calc(var1,var2,oper)
print(res)

#%% 3

import random

def getNumber():
    return random.randrange(1,46)

lotto=[]
num = 0

print("**로또 추첨을 사작합니다**\n")

while True:
    num=getNumber()
    
    if lotto.count(num)==0:
        lotto.append(num)
    if len(lotto)>=6:
        break
    
print("추첨된 로또 번호==> ",end='')
lotto.sort()
for i in range(0,6):
    print("%d "%lotto[i],end='')

#%% 4
import random
from tkinter.simpledialog import*

def getString():
    retStr=''
    retStr=askstring('문자열 입력','거북이 쓸 문자열을 입력')
    return retStr

def getRGB():
    r,g,b=0,0,0
    r=random.random()
    g=random.random()
    b=random.random()
    return(r,g,b)
    
def getXYAS(sw,sh):
    x,y,angle,size=0,0,0,0
    x=random.randrange(-sw/2,sw/2)
    y=random.randrange(-sh/2,sh/2)
    angle=random.randrange(0,360)
    size=random.randrange(10,50)
    return[x,y,angle,size]
#%% 5
import turtle

instr=''
swidth,sheight=300,300
tX,tY,tAngle,tSize=[0]*4

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.speed(20)

inStr=getString()

for ch in inStr:
    
    tX,tY,tAngle,txtSize=getXYAS(swidth,sheight)
    r,g,b=getRGB()
    
    turtle.goto(tX,tY)
    turtle.left(tAngle)
    
    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은고딕',txtSize,'bold'))
    
turtle.done()

#%% 6
myList=[1,2,3,4,5]
add10=lambda num:num+10
myList=list(map(add10,myList))
print(myList)

#%% 7
def selfCall():
    print('하',end='')
    selfCall()
selfCall()

#%% 8
def count(num):
    if num>=1:
        print(num,end=' ')
        count(num-1)
    else:
        print("")
count(10)
count(20)
#%% 9
def factorial(num):
    if num<=1:
        return num
    else:
        return num*factorial(num-1)
    
print(factorial(4))
print(factorial(10))

#%% 10
def getFunc():
    yield 1
    yield 2
    yield 3
    
print(list(getFunc()))

#%% 11
def genFunc(num):
    for i in range(0,num):
        yield i
        print('제너레이터 진행 중')
        
for data in genFunc(5):
    print(data)
    
#%% 12


def getNumber(strData):
    numStr=''
    for ch in strData:
        if ch.isdigit():
            numStr+=ch
        
    return int(numStr)
#%% 13
import random

data=[]
i,k=0,0

if __name__=="__main__":
    for i in range(0,10):
        tmp=hex(random.randrange(0,100000))
        tmp=tmp[2:]
        data.append(tmp)
    
    print('정렬전 데이터:',end=' ')
    [print(num,end=' ') for num in data]
    
    for i in range(0,len(data)-1):
        for k in range(i+1,len(data)):
            if getNumber(data[i]) > getNumber(data[k]):
                tmp=data[i]
                data[i]=data[k]
                data[k]=tmp
                
    
    print('\n정렬 후 데이터: ',end=' ')
    [print(num,end=' ') for num in data]
    
#%% 14
    
from time import *
from datetime import *

def countDays(date1,date2):
    retDays=0
    year,month,day=date1.split('/')
    sDay=date(int(year),int(month),int(day))
    year,month,day=date2.split('/')
    eDay=date(int(year),int(month),int(day))
    diffDays=eDay-sDay
    retDays=diffDays.days
    
    return retDays

def getDay(t):
    weeks=['월','화','수','목','금','토','일']
    return weeks[t.tm_wday]

startDate,curDate,tm='','',None

if __name__=="__main__":
    
    startDate=input('시작 날짜(연/월/일)-->')
    tm=localtime()
    curDate=str(tm.tm_year)+'/'+str(tm.tm_mon)+'/'+str(tm.tm_mday)
    
    print(startDate,'부터 오늘(',curDate,')까지는',countDays(startDate,curDate),'일이 지났습니다')
    print('그리고 오늘은 ',getDay(tm),'요일입니다')