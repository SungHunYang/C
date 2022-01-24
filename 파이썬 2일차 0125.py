
##a=int(input('정수 입력: '))
##print('짝수입니다.')  if a%2==0 else print('홀수입니다.')

# 제어문

# 조건문 vs 반복문

# 조건문: 분기점을 설정 / 양자택일
# 반복문: 계속진행 /N회 /여러번 수행 / 특정조건을 만족할때까지 계속

# if 문
# 2개의 if 문 -> 비교수행 2번
# 1개의 if 문 -> 비교수행 1번
# 들여쓰기는 enter누르면 자동으로 됨 안돼면 tab 하면 넘어간다.
a=int(input('정수 입력: '))
if a%2==0 :
    print('짝수입니다.')
else :
    print('홀수입니다.')

# 1번문제 정수 1개 입력  정수의 절대값은 10입니다
# 2번문제 정수 2개 입력  둘중의 더 큰 정수 값 뽑아 내기

N=int(input('정수 입력: '))
if N<0 :
    print('입력하신 정수의 절대값은',-N,'입니다')
else :
    print('입력하신 정수의 절대값은',N,'입니다')

num1=int(input('정수1 입력: '))
num2=int(input('정수2 입력: '))
if a==b:
    print('num1 과 num2 는 서로 같습니다.')
else : 
    if num1>num2 :
        print('둘중 더 큰수는',num1,'입니다')
    else :
        print('둘중 더 큰수는',num2,'입니다')
# print('둘중 더 큰수는',num1,'입니다') if num1>num2 else print('둘중 더 큰수는',num2,'입니다')
# 공백를 무시하고 넘기고 싶을때는 pass ex) if :  pass 이런식으로

name=input('아이디 입력: ')
pw=input('비밀번호 입력: ')

rootName='관리자'
rootPw='1234'

if name==rootName and pw==rootPw :
    print('관리자 로그인')
elif name==rootName and pw!=rootPw :
    print('관리자님 비밀번호 잊으셨어요?')
else :
    print(name+'님, 안녕하세요!')

# 1. 관리자 성공 2. 관리자 실패 3. 일반 사용자
# elif = else if 와 같다.

color=input('색입력(R/Y/G) :  ')

if color=='R' or color=='r':
    print('정지!')
elif color=='Y' or color=='y' :
    print('주의!')
elif color=='G' or color=='g' :
    print('출발!')
else : # 범위 밖 입력에 대해 안내 --> 유효성 검사
    print('잘못된 색깔 입력')







































