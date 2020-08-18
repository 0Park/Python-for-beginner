# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:51:53 2020

@author: Young Hun Park
"""

#%% first
i,k,guguLine=0,0,""

for i in range(2,10):
    guguLine=guguLine+("# %d단 #" %i)

print(guguLine)

for i in range(9,0,-1):
    guguLine =""
    for k in range(2,10):
        guguLine=guguLine+str("%2dX%2d=%2d" %(k,i,k*i))
        
    print(guguLine)
    
#%% second
i,k=0,0

i=0

while i<9:
    if i<5:
        k=0
        while k<4-i:
            print(' ',end='')
            k+=1
        k=0
        while k<i*2+1:
            print('\u2605',end='')
            k+=1
    else:
        k=0
        while k<i-4:
            print(' ',end='')
            k+=1
        k=0
        while k<(9-i)*2-1:
            print('\u2605',end='')
            k+=1
            
    print()
    i+=1

#%% third

numStr=""
size=0
ch=0

if __name__=="__main__":
    numStr=input("숫자를 여러 개 입력하세요: ")
    print("")
    
    
    size=len(numStr)
    for i in range(size):
        str=""
        ch=int(numStr[i])
        for j in range(ch):
          str=str+"\u2665"
        print(str)
        

#%% four

import turtle

i,k,tX,tY=[0]*4
swidth,sheight=800,450

if __name__=="__main__":
    turtle.title('거북 구구단')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    tX,tY=-500,250
    turtle.goto(tX,tY)
    
    for i in range(1,10):
        for k in range(2,10):
            turtle.goto(tX+80*k,tY-40*i)
            gugu=str(k)+' x '+str(i)+' = '+str(k*i)
            turtle.write(gugu,font=('Arial',12,'bold'))
    
    turtle.done()
        