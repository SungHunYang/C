
# 무한 루프== 무한반복문
# True 대입, 영원히 동작하는 반복문을 작성
#--> 디버깅중 강제 종료 ctrl+c(쉘)

# "종료 조건" 필요

i=0
while True :  
    if i==30:
        break # 즉시 해당하는 반복문의 바깥(마지막)으로 이동
    print(i, end=' ')
    i+=1

#예제1 정수 계속 입력  정수들의 총합이  100을 넘기면 종료
print()
print()
hap=0
cnt=0
while True :
    num=int(input('정수 입력 : '))
    cnt+=1
    hap+=num
    if hap>100 :
        print('입력값의 총합은 '+str(hap)+' 입니다')
        print('평균은',hap//cnt,'입니다.')
        break

# 예제2 0보다 작은 정수 입력 횟수
print()
cnt=0
while True :
    num=int(input('정수 입력 : '))
    if num<0 :
       cnt+=1
    elif num==0 :
        break
print('0보다 작은정수가',cnt,'번 입력됬습니다.')
#######################################
print()
cnt=0
while True :
    num=int(input('정수 입력 : '))
    if num>0 :
        continue # 반복문의 조건식으로 즉시이동(밑에 있는거 시행 x) --> 42번이동
    cnt+=1
    if num==0 :
        break  # 반복문의 바깥으로 즉시이동 --> 49번이동
print('0보다 작은정수가',cnt,'번 입력됬습니다.')

# 예제3 1번 누르면 따뜻한 커피 2번 차가운 커피 1 ,2 번 눌러야함 다른 번호 누르면 다시 돌아감
print()
while True :
    print('===메뉴판===')
    print('1. 따뜻한 커피', end='  ')
    print('2. 차가운 커피')
    print()
    num=int(input('원하는 메뉴 : '))
    if num<1 or num >2 :
            continue
    elif num==1 :
        print('따뜻한 커피 나왔습니다.')
        break
    else :
        print('차가운 커피 나왔습니다.')
        break




















