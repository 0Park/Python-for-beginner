# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:10:32 2020

@author: Young Hun Park
"""
#%% first cell
import turtle

swidth,sheight =500,500

turtle.title('무지기색 원그리기')
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.goto(0,-sheight/2)
turtle.pendown()
turtle.speed(100)

for radius in range(1,250):
    if radius %7 ==1:
        turtle.pencolor('red')
    elif radius % 7 ==2:
        turtle.pencolor('orange')
    elif radius % 7 ==3:
        turtle.pencolor('yellow')
    elif radius % 7 ==4:
        turtle.pencolor('green')
    elif radius % 7 ==5:
        turtle.pencolor('blue')
    elif radius % 7 ==6:
        turtle.pencolor('navyblue')
    else:
        turtle.pencolor('purple')
    
    turtle.circle(radius)
    
turtle.done()

#%% second
select,answer,numStr,num1,num2=0,0,"",0,0

select=int(input("1. 입력한 수식 계산 2.두 수 사이의 합계:"))

if select==1:
    numStr=input("*** 수식을 입력하세요: ")
    answer=eval(numStr)
    print("%s 결과는 %5.1f"%(numStr,answer))
elif select==2:
    num1=int(input("*** 첫 번째 숫자를 입력하세요:"))
    num2=int(input("*** 두 번째 숫자를 입력하세요:"))
    for i in range(num1,num2+1):
        answer=answer+i
        
    print("%d+...%d는 %d입니다." %(num1,num2,answer))
else:
    print("1또는 2만 입력해야 합니다.")
    
    
    
#%% third

num1=int(input("*** 첫 번째 숫자를 입력하세요:"))
num2=int(input("*** 두 번째 숫자를 입력하세요:"))
num3=int(input("더할 숫자를 입력하세요"))

a=int((num2-num1)/num3)
answer=num1
for i in range(1,a+1):
    answer+=num1+i*num3
print("결과 %d"%answer)