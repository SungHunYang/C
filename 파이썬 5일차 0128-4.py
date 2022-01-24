# [함수]
# 메서드. 메소드. method

# 1. input 2. 기능 3. output
# input 매개변수 인자 파라미터 인수 입력값
# output 반환값 return 리턴값 결과값 출력값


# input x output x
def func() : # 함수 선언. 정의
    print('함수를 호출합니다..')
# 코드의 재사용성 증

func() # 함수 호출


# input x output o

def func2():
    print('func2() 호출됨..')
    return 11 # 본인을 호출한 위치에 해당값을 '즉시'전달  -> 수행이 완료 이거 밑으로는 아무것도 수행 x

func2()
print(func2())
num=func2() # num에 11 저장

def f() :
    num=int(input('정수를 입력하세요 '))
    if num<0 :
        return num*(-1)
    return num

print(f())
# input o output x

def func3(x, y) :
    print('func3() 호출됨...')
    print('x=',x)
    print('y=',y)
func3(100,50)

def f2(a,b):
    print('-->',a**b) # 출력의 결과
f2(2,10)

# input o output o

def func4(x,y):
    return x**y # 실제 값으로 저장 // 뭘 할수있음 // 다른곳에 이용 가능 
print(func4(10,2)+2)  #--> 리턴이 있으면(func4에서 주는 값이 100이므로) 이런게 가능

    















