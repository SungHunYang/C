import random
# 중복 값을 없애기
xList=[]
for i in range(5):
    while True :
        num=random.randrange(1,6)
        if num not in xList:  ## xList 안에 num 이 없으면 break,, while 밖으로 나감
            break
    xList.append(num)

print(xList)

yList=[]

while True :
    num=random.randrange(1,6)
    if num not in yList :
        yList.append(num)
    if len(yList)==5 :
        break
print(yList)
# 반복문 <- 수행할 실제 행동을 잘 파악해라

#예제) 당첨 복권 1장 생성 랜덤번호 5개 (1~15) == 내껀 1~15 범위 에서 정수 입력
# 몇개의 번호가 맞는지 확인 1개당 1점 4~5점 당첨 나머지 꽝

lotto=[]
my=[]
for i in range(5):
    while True:
        num=random.randrange(1,16)
        if num not in lotto :
            lotto.append(num)
            break
lotto.sort()
for i in range(5):
    a=int(input('번호 입력 : '))
    my.append(a)
my.sort()
point=0    
for i in range(5):
    if my[i] == lotto[i] :
        point+=1
print(lotto)
print(my)
if point >=4 :
    print(point,'점 당첨')
elif point<4 :
    print(point,'점 꽝')

#in과 not in은 리스트, 튜플, 문자열에 해당 원소가 포함되어있는지 여부를 판단합니다











