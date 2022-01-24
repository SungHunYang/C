
# 필수 인자값 / 옵션 인자값

def f(a,b): # 필수 인자 값
    print('a=',a)
    print('b=',b)
print(f(1,2))

def f(a,b=1234): # 옵션 인자 값 'b' 선택 사항이 된거다
    # 옵션 인자 값은 "뒤에서 부터 넣어야 한다" a만 들어가면 오류 나옴 
    print('a=',a)
    print('b=',b)
print(f(1)) # 없으면 1234
print(f(1,2)) # 있으면 2

# 위치 인자값으로 함수를 호출 했다.
# 키워드 인자로 함수를 호출 할수도있다!
#ex)
f(b=20, a='apple')

# 정수 정수 문자열을 순서대로 값을 넣음 --> 10 10 * --> 100 부호가 없으면 무조건 더하기 
def op(a,b,o='+'):
    if o=='-':
        return a-b
    elif o=='*':
        return a*b
    elif o=='//':
        return a//b
    return a+b
print(op(20,30)) 
    



















