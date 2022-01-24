
xList=[10,20,30,40]

for i in range(len(xList)) :
    print(str(i+1)+'번째 값은'+str(xList[i])+'입니다')

for v in xList :
    print(v,end=' ')
print()

#예제) stuList=[] 성적을 입력 3번까지 화면 출력

stuList=[]
for i in range(3) :
    score=int(input(str(i+1)+'번째 학생 성적 : '))
    stuList.append(score) # 이렇게 값을 넣는거다. 그냥 stuList=input() 이렇게 하면 append 가 없어서 안들어간다.
for i in range(len(stuList)) :
    print(str(i+1)+' 번째 학생의 성적은 '+str(stuList[i])+' 입니다')

xList=[10,20,20,20,30]
i=0
while 20 in xList :
    xList.remove(20)
    print(i,'번',end=' ')
    i+=1
print()
print('청소 끝')
print(xList)

xList=[1,2,3,4,5,6,7]
# 슬라이싱
print(xList[2:5])# --> 앞은 포함되지만 뒤는 포함 되지 않음
print(xList[:4])#---> 맨앞에 '0'이 있는걸로 간주
print(xList[4:]) # --> 4번 부터 끝까지

yList=xList[4:] #---> 이런게 가능
print(yList)

# 정렬(sort())
import random
xList=[]
for i in range(10) :
    num=random.randrange(10,100)
    xList.append(num)

print(xList)
xList.sort()  #---> 같은 타입끼리 뭉쳐있을때 
print(xList)














