'''
# 정수를 2번 입력 함수로 입력 받음  다른 함수를 호출 하면 둘중 더 큰수 출력 두 숫자가 동일하면 '같습니다' 출력

def f1():
    num=int(input('정수 입력 : '))
    return num
a=f1()
b=f1()

def f2(a,b):
    if a<b :
        print('더 큰 값은 '+str(b))
    elif a>b:
        print('더 큰 값은 '+str(a))
    elif a==b:
        print('같습니다')
f2(a,b)
'''

# 재귀 함수 == 순환 함수 == 순환 호출
# : 본인의 기능을 수행하기 위해 자기 자신을 한번 더 부르는것
# : ex) 팩토리얼

# 무한루프와 유사하면 '종료조건'을 필요로 함

def fac(N):
    print('확인',N)
    if N==1:
        return 1
    return N*fac(N-1)
print(fac(5))

# show 를 재귀 함수로  변경 --> 1234 입력 4 3 2 1 로 뜨도록
def show(N) :
    print(N%10, end=' ')
    if N>=10:
        show(N//10)
print(show(1234))
































