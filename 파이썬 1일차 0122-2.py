# [연산자]

##산술연산자
# 나누기 / 몫 / 나머지

10/3 # 몫(실수) 다나옴
print(10/3)
10//3 # 몫(정수)
print(10//3)
10%3 # 나머지
print(10%3)

#곱 / 제곱
2*4 #곱
print(2*4)
2**4 #제곱
print(2**4)

## 복합대입연산자. 할당 연산자 . 누적 연산자
num=10
num=num+10
#연산자 2개
num+=10
#연산자 1개
num+=10
print(num)

## 비교연산자
# 질문이며, 대답을 리턴함 true false

## 논리연산자
# and , or, not(부정, 반대가 되서 출력)

#예제1) 정수 1번째 입력 정수 2번째 입력 1번째>2번째 --> 출력 1은 2보다 클까?  true false

a=int(input('a 정수입력: '))
b=int(input('b 정수입력: '))
print(a,'>',b,'?? ->',a>b)

## 식별연산자
# 두개의 값이 같은지 식별하는 연산자
# is  // a is b --> a가 b와 같니? true /false
# is not // a is not b--> a는 b가 아니니? true /false
'''
int 4byte(1byte==8bit)
1bit=0 or 1
num=10
00000000 00000000 00000000 00001010
2**23-1 까지 사용할수있다.
'''

## 삼항연산자 == 조건연산자
# a > b ? 1 : 2 --> a>b ? T : F 안 쓴다.
# print('결과가 참') if a>b else print('결과가 거짓')
# 조건식이 참이면 왼쪽 거짓이면 오른쪽

# 예제2) 정수 2개 입력 둘중 더 큰 정수는 __ 입니다.

num1=int(input('정수1 입력: '))
num2=int(input('정수2 입력: '))
print('둘 중 더 큰정수는',num1,'입니다') if num1>num2 else print('둘 중 더 큰정수는',num2,'입니다')

big= num1 if num1>num2 else num2 # --> 대입 연산자를 통해서도 가능

print('둘 중 더 큰정수는',big,'입니다')

# 파이썬은 들여쓰기 또한 문법이다.
# 처음에 띄어쓰기 조심할것





