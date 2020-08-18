# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:34:53 2020

@author: Young Hun Park
"""

#%% first

myList=[30,10,20]
print("현재 리스트:%s"%myList)

myList.append(40)
print("append(40)후의 리스트: %s"%myList)

print("pop()으로 추출한 값:%s"%myList.pop())
print("pop()후의 리스트:%s"%myList)

myList.sort()
print("sort()후의 리스트:%s"%myList)

myList.reverse()
print("reverse()후의 리스트:%s"%myList)

print("20값의 위치: %d"%myList.index(20))

myList.insert(2,222)
print("인서트후의 리스트:%s"%myList)

myList.remove(222)
print("remove후의 리스트:%s"%myList)

myList.extend([77,88,77])
print("extend이후의 리스트:%s"%myList)

print("77값의 개수:%d"%myList.count(77))

#%% second

import turtle
import random

myTurtle,tX,tY,tColor,tSize,tShape=[None]*6
shapeList=[]
playerTurtles=[]
swidth,sheight=500,500

if __name__=="__main__":
    turtle.title('거북 리스트 활용')
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)
    
    shapeList=turtle.getshapes()
    for i in range(0,100):
        random.shuffle(shapeList)
        myTurtle=turtle.Turtle(shapeList[0])
        tX=random.randrange(-swidth/2,swidth/2)
        tY=random.randrange(-sheight/2,sheight/2)
        r=random.random();g=random.random();b=random.random()
        tSize=random.randrange(1,3)
        playerTurtles.append([myTurtle,tX,tY,tSize,r,g,b])
        
    for tList in playerTurtles:
        myTurtle=tList[0]
        myTurtle.color((tList[4],tList[5],tList[6]))
        myTurtle.pencolor((tList[4],tList[5],tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1],tList[2])
    
    turtle.done()
    
#%% third
singer={}

singer['이름']='트와이스'
singer['구성원 수']=9
singer['데뷔']='서바이벌 식스틴'
singer['대표곡']='SIGNAL'

for k in singer.keys():
    print('%s --> %s'%(k,singer[k]))
    
#%% fourth
import operator

trainDic, trainList={},[]

trainDic={'Thomas':'토마스','Edward':'에드워드','Henry':'헨리','Gothen':'고든','James':'제임스'}
trainList=sorted(trainDic.items(),key=operator.itemgetter(0))

print(trainList)

#%% fifth
foods={"떡볶이":"오뎅",
       "짜짱면":"단무지",
       "라면":"김치",
       "피자":"피클",
       "맥주":"땅콩",
       "치킨":"치킨무",
       "삼겹살":"상추"}
while(True):
    myfood=input(str(list(foods.keys()))+"중 좋아하는 음식은?")
    if myfood in foods:
        print("<%s>궁합 음식은 <%s>입니다."%(myfood,foods.get(myfood)))
    elif myfood=="끝":
        break
    else:
        print("그런 음식이 없습니다. 확인해보세요.")

#%% 6
foods=['떡볶이','짜장면','라면','피자','맥주','치킨','삼겹살']
sides=['오뎅','단무지','김치']

for food,side in zip(foods,sides):
    print(food,'-->',side)
    
#%% 7

import random

data=[]
i,k=0,0

if __name__=="__main__":
    for i in range(0,10):
        tmp=hex(random.randrange(0,100000))
        data.append(tmp)
        
    print('정렬 전 데이터: ',end='')
    [print(num,end='')for num in data]
    
    for i in range(0,len(data)-1):
        for k in range(i+1,len(data)):
            if int(data[i],16)>int(data[k],16):
                tmp=data[i]
                data[i]=data[k]
                data[k]=tmp
                
    print('\n정렬 후 데이터: ',end='')
    [print(num,end='')for num in data]

#%% 8

import operator

trainTupleList=[('토마스',5),('헨리',8),('에드워드',9),('에밀리',5),('토마스',4),('헨리',7),('토마스',3),('에밀리',8),('퍼시',5),('고든',13)]
trainDic,trainList={},[]
tmpTup=None
totalRank,currentRank=1,1

if __name__=="__main__":
    for tmpTup in trainTupleList:
        tName=tmpTup[0]
        tweight=tmpTup[1]
        if tName in trainDic:
            trainDic[tName]+=tweight
        else:
            trainDic[tName]=tweight
        
    
    print('기차 수송량 목록 ==> ',trainTupleList)
    print('-------------------')
    trainList=sorted(trainDic.items(),key=operator.itemgetter(1),reverse=True)
    
    print('기차\t총 수송량\t순위')
    print('----------------------')
    print(trainList[0][0],'\t',trainList[0][1],'\t',currentRank)
    for i in range(1,len(trainList)):
        totalRank +=1
        if trainList[i][1]==trainList[i-1][1]:
            pass
        else:
            currentRank=totalRank
        print(trainList[i][0],'\t',trainList[i][1],'\t',currentRank)
    
            
    