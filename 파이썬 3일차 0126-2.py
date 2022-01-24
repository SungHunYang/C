
# for 문

for i in range(5):  # 디폴트로 시작점이 '0'으로 설정 range(4) 하면 3까지 즉 [i=0, i<4, i++] 이거다
    print(i,end='  ') # 이게 -1 개념이 아니라 포함하지 않는다는 개념이다!!

print()

for i in range(10,20):  # 이건 10~19 까지 즉 [i=10, i<20, i++]이다 // 앞은 포함o 뒤는 포함 x
    print(i,end='  ')

print()

for i in range(4,20,2): # 이건 2씩 증가 한다. 즉 range(초기값, 최종값, 증감식) 이다.
    print(i,end='  ')

print()
#예제 1) 정수1,2 입력: 둘의 사이값 나오게

a=int(input('정수1 입력: '))
b=int(input('정수2 입력: '))
if a>b :
      a,b=b,a

for i in range(a,b+1) :
      print(i,end='  ')

print()
# 예제 2) 정수 5번 입력 짝수 몇개

cnt=0
for i in range(5) :
    num=int(input('정수입력 : '))
    if num%2==1 :
        continue
    cnt+=1
print('짝수의 개수는',cnt)

# 예제 3) 구구단
# 이중 for문 == 중첩 반복문
for a in range(2,10) :         
    for i in range(1,10) :
        print(str(a)+'x'+str(i)+'=',a*i, end='  ')
    print()
    print('-----------------------------------')


# 예제4 별찍기

for a in range(5) : # (6, 1(+1) 까지) -->포함하지 않는다는 개념이니까 -1하면 1이 포함 되니까 2이다.
    for i in range(a) :
        print(' ',end=' ')
    for i in range(5-a) :
        print('*', end=' ')
    print()
    

















      
