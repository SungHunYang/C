age=int(input('나이를 입력 : '))

if age<=0 or 200<=age:
    print('입력한 값을 다시 확인해주세요')
elif age<=8 or age>=65 :
    fee=0
elif 9<=age and age<=19 :
    fee=1000
elif 20<=age and age<=64 :
    fee=2000
if 0<age and age<200 :
    print('당신의 요금은 '+str(fee)+' 입니다')


score=int(input('점수 입력: '))

if score<0 or score>100 :
    print('잘못된 입력입니다.')
elif score<=50 :
    grade='F'
elif score<=70 :
    grade='C'
elif score<=80 :
    grade='B'
elif 81<=score  and  score<=100 :
    grade='A'
if score>=0 and score<=100 :
    print('당신의 성적은 '+grade+' 입니다')

    
