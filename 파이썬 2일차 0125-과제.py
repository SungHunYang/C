'''
1. 정수 입력 하면 정수 입력된 값 까지의 총합
 입력 : 5   1~5 총합
 그런데 만일 음수로 입력하면 절대값 처리
 0을 입력했다면 수행없음을 띄울것

2. 현재 시, 분 입력  1시간 20분 전 시간 나오게 하기
범위 1~12시 0~59분
'''

a=int(input('정수 입력 : '))

if a<0 :
    a*=(-1)
elif a==0 :
    print('수행없음')
else :
    i=1
    hap=0
    while i<=a :
        hap+=i
        i+=1
    print(str(a)+'의 총합은 '+str(hap))


h=int(input('시 입력 : '))
m=int(input('분 입력 : '))
while 1 :
    if h<1 or h>24 :
        print('시간 오류')
        break
    if m<1 or m>59 :
        print('시간 오류')
        break
    elif  h>12 :
        h-=12
    print('현재시간은 '+str(h)+'시'+str(m)+'분 입니다')
    print('1시간 20분 전', end='   ')
    m-=20
    if m<0 :
        h-=1
        m+=60
    h-=1
    if h==0:
        h=12
    elif h<0 :
        h=11
    print(str(h)+'시'+str(m)+'분')
    break
        
    
    



