'''
문제1) 정수를 여러번 입력 짝수면 xList에 저장
0보다 작으면 절대값 처리해서 생각
0 이 입력되면 즉시종료 
'''

xList=[]

while True :
    num=int(input('정수 입력 : '))
    if num<0 :
        num*=(-1)
    elif num==0 :
        break
    elif num%2==0 :
        xList.append(num)
for i in range(len(xList)) :
    print('[',xList[i],']', end=' ')
print()
print('정렬하면')
xList.sort()
for i in range(len(xList)) :
    print('[',xList[i],']', end=' ')
print()
# 최대값 찾기 알고리즘

xList=[2,4,1,5,3]
m=xList[0]
for v in xList :
    if m<v :
        m=v
print('최대값은',m,'입니다')

# 예제)
import random

xList=[]
s=100
for i in range(5) :
    num=random.randrange(1,101)
    xList.append(num)
for i in range(len(xList)) :
    if s>xList[i]:
        s=xList[i]
        n=i
for v in xList :
    print(v,end=' ')
print()
print('최소값은',s,'이고 인덱스 번호는',n,'번 입니다')
    
# 리스트의 모든 홀수를 제거 
xList=[1,2,3,4,5]
i=0

while  i<len(xList) :
    if xList[i]%2==1:
        del xList[i]
    else:
        i+=1
print(xList)














