# 반복문
# : 코드의 재사용성 증가

# while    vs      for

# while
# 불분명한 반복 횟수
# for
# 명확한 반복횟수/ 범위가 주어진 경우의 수행
i=0
while i<3 :
    print('i=',i)
    i+=1
print('최종 i=',i)

#예제1 정수 입력 1~ 해당 정수 까지 출력

a=int(input('정수1 입력 : '))
b=int(input('정수2 입력 : '))
if b<a :
    #값 교환
    a,b=b,a

while a<=b :
    print('i=',a ,end='  ')
    a+=1
print()

i=0
cnt=0
while i<5:
    num=int(input('정수입력 : '))
    if num%2==1:
        cnt+=1
    i+=1             
print('홀수의 개수는',cnt,'입니다')




